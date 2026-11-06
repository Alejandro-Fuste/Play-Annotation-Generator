# Play-Annotation-Generator Annotation Review — OutsideZoneRead_101

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_101`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | CB2 | defense | `17` | `16` |
| ✅ EXACT | `Action_ReadEdgeDefender` | CB2 | defense | `17` | `16` |
| ✅ EXACT | `Action_Keep` | CB2 | defense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB2 | defense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 1 | START | 1 | 7 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `14` | 4 | START | 8 | 39 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `16` | `15` | 4 | START | 4 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 4 | START | 4 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `20` | 4 | START | 4 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 4 | START | 4 | 19 |
| ✅ EXACT | `Action_SnapReceive` | CB2 | `17` | `16` | 7 | END | 1 | 7 |
| ✅ EXACT | `Action_ReadEdgeDefender` | CB2 | `17` | `16` | 10 | START | 10 | 24 |
| ✅ EXACT | `Action_Keep` | CB2 | `17` | `16` | 25 | START | 25 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | CB2 | `17` | `16` | 34 | START | 34 | 140 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 60 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 12 | 12 | inferred_complete_timeline |
| `Action_None` | 14 | 180 | 167 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 60 | 57 | inferred_complete_timeline |
| `Action_None` | 61 | 180 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 42 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 59 | 60 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 7 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 8 | 39 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 41 | 60 | 20 | inferred_complete_timeline |
| `Action_None` | 61 | 180 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 19 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 43 | 57 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 26 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 32 | 52 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 55 | 60 | 6 | inferred_complete_timeline |
| `Action_None` | 61 | 180 | 120 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 36 | 36 | inferred_complete_timeline |
| `Action_None` | 41 | 44 | 4 | inferred_complete_timeline |
| `Action_None` | 47 | 74 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 82 | 82 | inferred_complete_timeline |
| `Action_None` | 100 | 180 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 10 | 10 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 104 | 104 | inferred_complete_timeline |
| `Action_None` | 109 | 180 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 180 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 7 | 7 | inferred_complete_timeline |
| `Action_None` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 10 | 24 | 15 | inferred_complete_timeline |
| `Action_Keep` | 25 | 33 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 34 | 140 | 107 | inferred_complete_timeline |
| `Action_BallCarry` | 148 | 152 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 157 | 158 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 165 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 148 | 148 | inferred_complete_timeline |
| `Action_None` | 152 | 180 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 127 | 127 | inferred_complete_timeline |
| `Action_None` | 130 | 180 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–61 | 62 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 53–180 | 93 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 64–68 | 5 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 74–180 | 107 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 74–180 | 100 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 83–180 | 83 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 89–90 | 2 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 94–137 | 17 | 4 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 167–169 | 3 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 175–180 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 204: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [1–7], lower_priority='Action_ZoneBlock' annotated_start=4, effective_Action_ZoneBlock_start=8.
- ⚠️ Action 'Action_None' range [1-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-104] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-36] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-44] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-61] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-165] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [8-39] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [34-140] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [148-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [157-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-10] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-26] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-30] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [32-52] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-12] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-42] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [59-60] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-19] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-26] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [43-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-84] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-180] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-134] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-148] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-100] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-180] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-90] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>