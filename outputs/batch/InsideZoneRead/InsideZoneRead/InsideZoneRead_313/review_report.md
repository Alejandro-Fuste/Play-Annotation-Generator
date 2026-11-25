# Play-Annotation-Generator Annotation Review — InsideZoneRead_313

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_313`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 130
- **Validation Warnings:** 138
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 104
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE1 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_Keep` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LT | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `2` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_BallSnap` | DE1 | `9` | `8` | 5 | START | 5 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `14` | 8 | START | 8 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `15` | 8 | START | 8 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 8 | START | 8 | 38 |
| ✅ EXACT | `Action_ZoneBlock` | C | `20` | `19` | 8 | START | 8 | 28 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `6` | `5` | 8 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | LT | `6` | `5` | 19 | END | 5 | 19 |
| ✅ EXACT | `Action_ReadDefender` | LT | `6` | `5` | 26 | START | 26 | 35 |
| ✅ EXACT | `Action_Keep` | LT | `6` | `5` | 36 | START | 36 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LT | `6` | `5` | 59 | START | 59 | 91 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 96 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 89 | 85 | inferred_complete_timeline |
| `Action_None` | 91 | 100 | 10 | inferred_complete_timeline |
| `Action_None` | 104 | 126 | 23 | inferred_complete_timeline |
| `Action_None` | 131 | 155 | 25 | inferred_complete_timeline |
| `Action_None` | 163 | 180 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 48 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 63 | 59 | inferred_complete_timeline |
| `Action_None` | 68 | 89 | 22 | inferred_complete_timeline |
| `Action_None` | 95 | 99 | 5 | inferred_complete_timeline |
| `Action_None` | 104 | 128 | 25 | inferred_complete_timeline |
| `Action_None` | 131 | 161 | 31 | inferred_complete_timeline |
| `Action_None` | 163 | 180 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 180 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 180 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 98 | 94 | inferred_complete_timeline |
| `Action_None` | 105 | 180 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 19 | 15 | inferred_complete_timeline |
| `Action_None` | 20 | 25 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 26 | 35 | 10 | inferred_complete_timeline |
| `Action_Keep` | 36 | 58 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 59 | 91 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 180 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 38 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 48 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 53 | 67 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 96 | 28 | inferred_complete_timeline |
| `Action_None` | 97 | 135 | 39 | inferred_complete_timeline |
| `Action_None` | 140 | 180 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 28 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 49 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 52 | 61 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 60 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 89 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 96 | 5 | inferred_complete_timeline |
| `Action_None` | 97 | 180 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 5 | 19 | 15 | inferred_complete_timeline |
| `Action_None` | 20 | 51 | 32 | inferred_complete_timeline |
| `Action_None` | 53 | 58 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–27
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 27 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 58 | 54 | inferred_complete_timeline |
| `Action_None` | 68 | 180 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 39 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 76 | 72 | inferred_complete_timeline |
| `Action_None` | 85 | 89 | 5 | inferred_complete_timeline |
| `Action_None` | 137 | 180 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 44 | 40 | inferred_complete_timeline |
| `Action_None` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_None` | 59 | 61 | 3 | inferred_complete_timeline |
| `Action_None` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_None` | 102 | 180 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 180 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 113 | 109 | inferred_complete_timeline |
| `Action_None` | 119 | 135 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 97 | 93 | inferred_complete_timeline |
| `Action_None` | 120 | 131 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 32 | 28 | inferred_complete_timeline |
| `Action_None` | 35 | 36 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 53 | 10 | inferred_complete_timeline |
| `Action_None` | 56 | 57 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 165 | 161 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–145 | 78 | 9 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 17–180 | 68 | 8 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 31–59 | 11 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 54–113 | 52 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 77–180 | 104 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 77–180 | 104 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 85–93 | 5 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 93–108 | 13 | 2 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 108–118 | 4 | 2 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 123–180 | 58 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 124–170 | 43 | 3 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 131–180 | 38 | 6 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 132–180 | 49 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 138–180 | 43 | 1 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 141–180 | 40 | 1 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 152–157 | 6 | 1 | Undefined position; Undefined team |
| `38` | `58` | Position_Unknown | Team_Unknown | 173–180 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (5 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `6` (LT)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 101 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '5' has invalid range: start=8, end=4. Clamping end to start.
- ⚠️ Action 'Action_None' range [5-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-63] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-89] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-128] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-180] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-32] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-36] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-53] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-98] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [59-91] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [97-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-135] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-89] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-126] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-155] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-58] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-165] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-97] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-58] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-180] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-180] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [52-61] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-76] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-38] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [41-48] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [53-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-28] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-27] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-44] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-71] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-20] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-73] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-104] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-33] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-155] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-36] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-71] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-89] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-100] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-101] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-157] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-170] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-136] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-151] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-180] for track '35' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-180] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_313'; source metadata written as null.

</details>