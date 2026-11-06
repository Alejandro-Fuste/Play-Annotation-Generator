# Play-Annotation-Generator Annotation Review — OutsideZoneRead_141

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_141`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 65
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `11` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `23` | `22` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Keep` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `18` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `19` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `23` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 18 | START | 18 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `10` | `9` | 21 | START | 21 | 40 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `11` | `10` | 21 | START | 21 | 104 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `21` | `20` | 21 | START | 38 | 104 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `23` | `22` | 21 | START | 21 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `5` | `4` | 21 | START | 21 | 34 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 37 | END | 18 | 37 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `16` | `15` | 40 | START | 40 | 41 |
| ✅ EXACT | `Action_Keep` | QB | `16` | `15` | 42 | START | 42 | 55 |
| ✅ EXACT | `Action_BallCarry` | QB | `16` | `15` | 56 | START | 56 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 104 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 37 | 20 | inferred_complete_timeline |
| `Action_None` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_Keep` | 42 | 55 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 56 | 180 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 137 | 120 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 180 | 163 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 180 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 180 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 127 | 110 | inferred_complete_timeline |
| `Action_None` | 130 | 180 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 104 | 84 | inferred_complete_timeline |
| `Action_None` | 105 | 180 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 104 | 84 | inferred_complete_timeline |
| `Action_None` | 105 | 158 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_BallSnap` | 18 | 37 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 38 | 104 | 67 | inferred_complete_timeline |
| `Action_None` | 105 | 150 | 46 | inferred_complete_timeline |
| `Action_None` | 152 | 159 | 8 | inferred_complete_timeline |
| `Action_None` | 161 | 180 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 104 | 63 | inferred_complete_timeline |
| `Action_None` | 105 | 117 | 13 | inferred_complete_timeline |
| `Action_None` | 119 | 180 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 40 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 180 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 59 | 42 | inferred_complete_timeline |
| `Action_None` | 64 | 158 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 123 | 106 | inferred_complete_timeline |
| `Action_None` | 129 | 180 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 67 | 50 | inferred_complete_timeline |
| `Action_None` | 69 | 89 | 21 | inferred_complete_timeline |
| `Action_None` | 91 | 129 | 39 | inferred_complete_timeline |
| `Action_None` | 132 | 150 | 19 | inferred_complete_timeline |
| `Action_None` | 155 | 175 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 89 | 72 | inferred_complete_timeline |
| `Action_None` | 91 | 180 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 91 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 180 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 180 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 180 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 117 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 156 | 139 | inferred_complete_timeline |
| `Action_None` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 180 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–124 | 88 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 56–180 | 123 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 99–180 | 82 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 126–127 | 2 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 141–142 | 2 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 143–156 | 14 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 153–180 | 28 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `21` (C): Annotated start 21 != Inferred start 38
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [18–37], lower_priority='Action_ZoneBlock' annotated_start=21, effective_Action_ZoneBlock_start=38.
- ⚠️ Action 'Action_None' range [18-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-117] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-34] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-117] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-67] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-89] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-129] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-175] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-59] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-40] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-123] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-89] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-137] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [56-180] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-156] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-180] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-61] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-156] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>