# Play-Annotation-Generator Annotation Review — Post10to15_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_53`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR3 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `19` | `19` | 21 | START | 21 | 30 |
| ✅ EXACT | `Action_PassBlock` | LT | `10` | `10` | 24 | START | 24 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `15` | `15` | 24 | START | 24 | 64 |
| ✅ EXACT | `Action_PassBlock` | RT | `18` | `18` | 24 | START | 24 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 24 | START | 42 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 24 | START | 24 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR3 | `2` | `2` | 41 | START | 41 | 174 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 41 | END | 21 | 41 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 69 | START | 69 | 78 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 41 | 21 | inferred_complete_timeline |
| `Action_None` | 42 | 47 | 6 | inferred_complete_timeline |
| `Action_None` | 57 | 68 | 12 | inferred_complete_timeline |
| `Action_ThrowPass` | 69 | 78 | 10 | inferred_complete_timeline |
| `Action_None` | 79 | 106 | 28 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 115 | 142 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 177 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_RunPostRoute` | 41 | 174 | 134 | inferred_complete_timeline |
| `Action_RunPostRoute` | 177 | 179 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 68 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 180 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 72 | 49 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 180 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 21 | 30 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 41 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 46 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 51 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 62 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 105 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 107 | 180 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 64 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 180 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 24 | 74 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 68 | 48 | inferred_complete_timeline |
| `Action_None` | 75 | 82 | 8 | inferred_complete_timeline |
| `Action_None` | 84 | 88 | 5 | inferred_complete_timeline |
| `Action_None` | 91 | 93 | 3 | inferred_complete_timeline |
| `Action_None` | 97 | 180 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 78 | 58 | inferred_complete_timeline |
| `Action_None` | 85 | 111 | 27 | inferred_complete_timeline |
| `Action_None` | 115 | 180 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 38 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 96 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 110 | 90 | inferred_complete_timeline |
| `Action_None` | 114 | 180 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 86 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 162 | 142 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 116 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 157 | 137 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 70–180 | 107 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 86–180 | 90 | 5 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 116–166 | 50 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 127–180 | 54 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 132–134 | 3 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 158–172 | 15 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 164–180 | 17 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 170–180 | 11 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 176–180 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunPostRoute` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [21–41], lower_priority='Action_PassBlock' annotated_start=24, effective_Action_PassBlock_start=42.
- ⚠️ Action 'Action_None' range [21-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [41-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [177-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-68] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-110] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-162] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-180] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-68] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-96] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-177] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-74] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [21-30] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-51] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-105] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [107-180] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [24-72] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-180] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-111] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-110] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-109] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-166] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-172] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-180] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '30' has 1 frames without a visible bounding box.
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