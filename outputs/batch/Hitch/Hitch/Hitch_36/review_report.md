# Play-Annotation-Generator Annotation Review — Hitch_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Hitch_36`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Hitch`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 168
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 112
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `19` | `19` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_RunHitchRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 1 | START | 1 | 10 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `12` | `12` | 4 | START | 4 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `16` | `16` | 4 | START | 4 | 77 |
| ✅ EXACT | `Action_PassBlock` | LT | `19` | `19` | 4 | START | 4 | 63 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `20` | `20` | 4 | START | 11 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `4` | `4` | 4 | START | 4 | 73 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 10 | END | 1 | 10 |
| ✅ EXACT | `Action_RunHitchRoute` | WR1 | `0` | `0` | 19 | START | 19 | 82 |
| ✅ EXACT | `Action_ThrowPass` | QB | `7` | `7` | 67 | START | 67 | 76 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `0` | `0` | 119 | START | 119 | 153 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 10 | 10 | inferred_complete_timeline |
| `Action_None` | 11 | 30 | 20 | inferred_complete_timeline |
| `Action_None` | 32 | 66 | 35 | inferred_complete_timeline |
| `Action_ThrowPass` | 67 | 76 | 10 | inferred_complete_timeline |
| `Action_None` | 77 | 210 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 124 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_RunHitchRoute` | 19 | 82 | 64 | inferred_complete_timeline |
| `Action_None` | 83 | 118 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 119 | 153 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 52 | 52 | inferred_complete_timeline |
| `Action_None` | 60 | 123 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 118 | 118 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 162 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 63 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 117 | 114 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 125 | 128 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 10 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 122 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 77 | 74 | inferred_complete_timeline |
| `Action_PassBlock` | 84 | 91 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 115 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 4 | 73 | 70 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 164 | 90 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 60 | 60 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 74 | 78 | 5 | inferred_complete_timeline |
| `Action_None` | 81 | 88 | 8 | inferred_complete_timeline |
| `Action_None` | 93 | 100 | 8 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 41 | 41 | inferred_complete_timeline |
| `Action_None` | 43 | 48 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–35
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 30 | 30 | inferred_complete_timeline |
| `Action_None` | 34 | 35 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 43 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 71 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 111 | 111 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 171 | 171 | inferred_complete_timeline |
| `Action_None` | 174 | 188 | 15 | inferred_complete_timeline |
| `Action_None` | 198 | 204 | 7 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 210 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 172 | 172 | inferred_complete_timeline |
| `Action_None` | 177 | 210 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 114 | 114 | inferred_complete_timeline |
| `Action_None` | 116 | 123 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 2–155 | 111 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 17–147 | 95 | 8 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 41–43 | 3 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 71–210 | 139 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 78–210 | 110 | 7 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 105–210 | 105 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 107–210 | 104 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 107–110 | 4 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 121–203 | 70 | 5 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 127–149 | 18 | 4 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 131–179 | 46 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 141–210 | 70 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 142–144 | 3 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 150–210 | 61 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 151–153 | 3 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 151–210 | 60 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 152–158 | 7 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 153–210 | 58 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 154–203 | 28 | 4 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 157–201 | 40 | 2 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 166–169 | 4 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 180–182 | 3 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 180–210 | 31 | 1 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 192–210 | 15 | 2 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 196–210 | 13 | 2 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 201–210 | 10 | 1 | Undefined position; Undefined team |
| `48` | `64` | Position_Unknown | Team_Unknown | 202–207 | 6 | 1 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `50` | `67` | Position_Unknown | Team_Unknown | 207–210 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (3 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `20` (C): Annotated start 4 != Inferred start 11
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 106 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [1–10], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=11.
- ⚠️ Action 'Action_BallCarry' range [119-153] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-118] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-162] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-164] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-43] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-60] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-88] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-30] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-172] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-171] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-188] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-117] for track '12' has 10 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [125-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-52] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-123] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-111] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-48] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [84-91] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-114] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-123] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-30] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [4-63] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-122] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-72] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-155] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-29] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-38] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-49] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-74] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-103] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-113] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-121] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-147] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-91] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-137] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-158] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-110] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-147] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-159] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-181] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-190] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-146] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-172] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-181] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-181] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-201] for track '41' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '47' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.

</details>