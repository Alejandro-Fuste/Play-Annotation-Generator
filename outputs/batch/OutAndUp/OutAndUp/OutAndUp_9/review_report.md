# Play-Annotation-Generator Annotation Review — OutAndUp_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutAndUp_9`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutAndUp`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | LB2 | defense | `16` | `16` |
| ✅ EXACT | `Action_SellOut` | WR4 | offense | `0` | `0` |
| ✅ EXACT | `Action_RunGoRoute` | WR4 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | LB2 | defense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 6 | START | 6 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `10` | `10` | 9 | START | 9 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `18` | `18` | 9 | START | 9 | 147 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 9 | START | 9 | 155 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 9 | START | 25 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 9 | START | 9 | 48 |
| ✅ EXACT | `Action_SnapReceive` | LB2 | `16` | `16` | 24 | END | 6 | 24 |
| ✅ EXACT | `Action_SellOut` | WR4 | `0` | `0` | 57 | START | 57 | 92 |
| ✅ EXACT | `Action_RunGoRoute` | WR4 | `0` | `0` | 93 | START | 93 | 210 |
| ✅ EXACT | `Action_ThrowPass` | LB2 | `16` | `16` | 112 | START | 112 | 124 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 140 | 135 | inferred_complete_timeline |
| `Action_None` | 142 | 144 | 3 | inferred_complete_timeline |
| `Action_None` | 149 | 158 | 10 | inferred_complete_timeline |
| `Action_None` | 165 | 192 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 72 | 67 | inferred_complete_timeline |
| `Action_None` | 76 | 210 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 127 | 122 | inferred_complete_timeline |
| `Action_None` | 129 | 210 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_SellOut` | 57 | 92 | 36 | inferred_complete_timeline |
| `Action_RunGoRoute` | 93 | 210 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 147 | 139 | inferred_complete_timeline |
| `Action_PassBlock` | 151 | 165 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 167 | 170 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 155 | 147 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 168 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 6 | 24 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 33 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 42 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 66 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 165 | 91 | inferred_complete_timeline |
| `Action_PassBlock` | 170 | 185 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 187 | 192 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 194 | 204 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 48 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 56 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 100 | 92 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 199 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 115 | 110 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 95 | 90 | inferred_complete_timeline |
| `Action_None` | 98 | 120 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 159 | 154 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 140 | 135 | inferred_complete_timeline |
| `Action_None` | 142 | 149 | 8 | inferred_complete_timeline |
| `Action_None` | 151 | 210 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 6 | 24 | 19 | inferred_complete_timeline |
| `Action_None` | 25 | 111 | 87 | inferred_complete_timeline |
| `Action_ThrowPass` | 112 | 124 | 13 | inferred_complete_timeline |
| `Action_None` | 125 | 129 | 5 | inferred_complete_timeline |
| `Action_None` | 132 | 210 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 210 | 205 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–210 | 210 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 43–60 | 18 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 48–210 | 143 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 88–113 | 14 | 3 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 107–112 | 6 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 121–135 | 15 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 121–122 | 2 | 1 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 133–150 | 14 | 2 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 136–185 | 8 | 4 | Undefined position; Undefined team |
| `30` | `50` | Position_Unknown | Team_Unknown | 145–188 | 41 | 2 | Undefined position; Undefined team |
| `31` | `52` | Position_Unknown | Team_Unknown | 149–152 | 4 | 1 | Undefined position; Undefined team |
| `32` | `53` | Position_Unknown | Team_Unknown | 150–159 | 6 | 2 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 150–151 | 2 | 1 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 151–152 | 2 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 156–170 | 9 | 3 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 157–210 | 53 | 2 | Undefined position; Undefined team |
| `37` | `62` | Position_Unknown | Team_Unknown | 179–207 | 29 | 1 | Undefined position; Undefined team |
| `38` | `64` | Position_Unknown | Team_Unknown | 184–210 | 27 | 1 | Undefined position; Undefined team |
| `39` | `68` | Position_Unknown | Team_Unknown | 191–210 | 18 | 3 | Undefined position; Undefined team |
| `40` | `73` | Position_Unknown | Team_Unknown | 202–210 | 9 | 1 | Undefined position; Undefined team |
| `41` | `74` | Position_Unknown | Team_Unknown | 203–210 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (8 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 12: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [6–24], lower_priority='Action_PassBlock' annotated_start=9, effective_Action_PassBlock_start=25.
- ⚠️ Action 'Action_RunGoRoute' range [93-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-95] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-120] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-140] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-149] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-64] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-140] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-158] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-192] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-159] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-115] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-199] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [151-165] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [167-170] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-155] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-33] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-42] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-66] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-165] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [170-185] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [187-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [194-204] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [206-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-60] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-149] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-184] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-101] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-112] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-135] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-144] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-178] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-188] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-164] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-170] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-207] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-210] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>