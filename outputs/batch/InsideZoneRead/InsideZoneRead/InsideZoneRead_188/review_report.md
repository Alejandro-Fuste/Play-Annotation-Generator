# Play-Annotation-Generator Annotation Review — InsideZoneRead_188

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_188`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 137
- **Validation Warnings:** 176
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 5
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 116
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | SAF2 | defense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | SAF2 | defense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | DT1 | defense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | SAF2 | defense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LB3 | defense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 12 | START | 3 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `15` | `Group` | 12 | START | 3 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 12 | START | 3 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 12 | START | 3 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `18` | `Group` | 12 | START | 3 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 12 | START | 3 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 12 | START | 3 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 12 | START | 3 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 12 | START | 3 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 12 | START | 3 | 11 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `8` | `7` | 39 | START | 39 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `16` | `15` | 42 | START | 74 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `17` | `16` | 42 | START | 88 | 89 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `19` | `18` | 42 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `20` | `19` | 42 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `22` | `21` | 42 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | SAF2 | `9` | `8` | 51 | END | 39 | 51 |
| ✅ EXACT | `Action_ReadDefender` | SAF2 | `9` | `8` | 56 | START | 56 | 70 |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | DT1 | `7` | `6` | 65 | START | N/A | N/A |
| ✅ EXACT | `Action_Handoff` | SAF2 | `9` | `8` | 71 | START | 71 | 82 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | LB3 | `10` | `9` | 83 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 125 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 3–24
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 24 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 3–199
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 38 | 36 | inferred_complete_timeline |
| `Action_None` | 39 | 199 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 3–47
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 38 | 36 | inferred_complete_timeline |
| `Action_None` | 39 | 47 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 3–11
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 3–199
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 38 | 36 | inferred_complete_timeline |
| `Action_None` | 39 | 42 | 4 | inferred_complete_timeline |
| `Action_None` | 46 | 105 | 60 | inferred_complete_timeline |
| `Action_None` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 115 | 119 | 5 | inferred_complete_timeline |
| `Action_None` | 122 | 126 | 5 | inferred_complete_timeline |
| `Action_None` | 128 | 199 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 3–196
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 119 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_None` | 126 | 126 | 1 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_None` | 169 | 196 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 3–101
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 101 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 3–19
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 19 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 3–15
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 15 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 3–11
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–41
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 22 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 33 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_None` | 40 | 41 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–11
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–11
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 3–16
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 11 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 16 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–156
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 38 | 36 | inferred_complete_timeline |
| `Action_None` | 39 | 106 | 68 | inferred_complete_timeline |
| `Action_None` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_None` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–149
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 38 | 36 | inferred_complete_timeline |
| `Action_None` | 39 | 131 | 93 | inferred_complete_timeline |
| `Action_None` | 133 | 139 | 7 | inferred_complete_timeline |
| `Action_None` | 145 | 149 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–56
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 38 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 56 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–199
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 38 | 36 | inferred_complete_timeline |
| `Action_None` | 39 | 199 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 3–184
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 38 | 36 | inferred_complete_timeline |
| `Action_None` | 39 | 184 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–199
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 38 | 36 | inferred_complete_timeline |
| `Action_None` | 39 | 180 | 142 | inferred_complete_timeline |
| `Action_None` | 196 | 199 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–156
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 38 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 39 | 51 | 13 | inferred_complete_timeline |
| `Action_None` | 52 | 55 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 56 | 70 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 71 | 82 | 12 | inferred_complete_timeline |
| `Action_None` | 83 | 130 | 48 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `8` | Position_Unknown | Team_Unknown | 3–180 | 145 | 11 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 28–111 | 82 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 38–51 | 14 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 46–62 | 15 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 54–196 | 134 | 5 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 76–199 | 84 | 8 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 77–126 | 20 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 86–91 | 6 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 87–90 | 4 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 87–180 | 91 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 117–199 | 82 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 123–199 | 73 | 4 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 123–199 | 35 | 7 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 123–176 | 33 | 3 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 124–127 | 4 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 124–126 | 3 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 124–125 | 2 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 154–195 | 27 | 5 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 154–196 | 39 | 3 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 170–199 | 25 | 3 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 171–196 | 25 | 2 | Undefined position; Undefined team |
| `42` | `50` | Position_Unknown | Team_Unknown | 174–196 | 22 | 2 | Undefined position; Undefined team |
| `43` | `51` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `44` | `52` | Position_Unknown | Team_Unknown | 198–199 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `19` (RT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `20` (C)
- ❌ Missing segment for action `Action_ZoneBlock` on target `22` (RG)
- ❌ Missing segment for action `Action_BlockSecondLevel` on target `7` (DT1)
- ❌ Missing segment for action `Action_BallCarry` on target `10` (LB3)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 120 |
| Track-related warning | 6 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 375: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '6' has invalid range: start=65, end=11. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '9' has invalid range: start=83, end=56. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '18' has invalid range: start=42, end=11. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '19' has invalid range: start=42, end=19. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=42, end=15. Clamping end to start.
- ⚠️ Action 'Action_None' range [39-199] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-47] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-106] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-199] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-155] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-38] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-56] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-131] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-22] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-33] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-184] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 126, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [126-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-196] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [88-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-101] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-42] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-105] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-199] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-19] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-24] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-11] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-33] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-48] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-51] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-52] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-62] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-56] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-103] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-190] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-90] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-109] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-166] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-199] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-126] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-91] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-175] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-199] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-199] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-185] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-160] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-176] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-127] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-166] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-187] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-185] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-199] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-192] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-191] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_188'; source metadata written as null.

</details>