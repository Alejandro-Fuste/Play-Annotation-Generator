# Play-Annotation-Generator Annotation Review — Counter_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_67`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `19` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `21` | `20` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 37 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 38 | START | 38 | 51 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `14` | `13` | 41 | START | 52 | 127 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `3` | `2` | 41 | START | 41 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `19` | `18` | 46 | START | 46 | 92 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `20` | 51 | END | 38 | 51 |
| ✅ EXACT | `Action_Handoff` | QB | `21` | `20` | 63 | START | 63 | 81 |
| ✅ EXACT | `Action_BallCarry` | RB | `22` | `21` | 82 | START | 82 | 202 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 127 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_SnapReceive` | 38 | 51 | 14 | inferred_complete_timeline |
| `Action_None` | 52 | 62 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 63 | 81 | 19 | inferred_complete_timeline |
| `Action_None` | 82 | 210 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_BallCarry` | 82 | 202 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 210 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 210 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 138 | 101 | inferred_complete_timeline |
| `Action_None` | 140 | 210 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 41 | 127 | 87 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 106 | 69 | inferred_complete_timeline |
| `Action_None` | 108 | 210 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 50 | 13 | inferred_complete_timeline |
| `Action_None` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_None` | 72 | 210 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_BallSnap` | 38 | 51 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 52 | 127 | 76 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 46 | 92 | 47 | inferred_complete_timeline |
| `Action_PullBlock` | 94 | 110 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 210 | 173 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 125 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 75 | 38 | inferred_complete_timeline |
| `Action_None` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_None` | 87 | 210 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 94 | 57 | inferred_complete_timeline |
| `Action_None` | 99 | 210 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 77 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 83 | 46 | inferred_complete_timeline |
| `Action_None` | 86 | 151 | 66 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 210 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 101 | 64 | inferred_complete_timeline |
| `Action_None` | 110 | 144 | 35 | inferred_complete_timeline |
| `Action_None` | 146 | 210 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 200 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 210 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 210 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 187 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 210 | 173 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 49–50 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 70–113 | 13 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 74–75 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 77–210 | 134 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 97–106 | 10 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 114–133 | 19 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 132–210 | 73 | 3 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 140–210 | 69 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 147–150 | 4 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 194–206 | 9 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 204–209 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `14` (C): Annotated start 41 != Inferred start 52
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [38–51], lower_priority='Action_DownBlock' annotated_start=41, effective_Action_DownBlock_start=52.
- ⚠️ Action 'Action_None' range [38-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-187] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-77] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-106] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-200] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-75] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-50] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-210] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [46-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [94-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [82-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-75] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-106] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-129] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-155] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '32' has 1 frames without a visible bounding box.
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

</details>