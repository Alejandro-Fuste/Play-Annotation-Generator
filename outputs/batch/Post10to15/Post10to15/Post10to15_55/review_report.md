# Play-Annotation-Generator Annotation Review — Post10to15_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_55`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 88
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
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_RunPostRoute` | WR4 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 17 | START | 17 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 20 | START | 20 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 20 | START | 20 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 20 | START | 31 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 20 | START | 20 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `4` | `4` | 20 | START | 20 | 83 |
| ✅ EXACT | `Action_RunPostRoute` | WR4 | `3` | `3` | 30 | START | 30 | 180 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 30 | END | 17 | 30 |
| ✅ EXACT | `Action_ThrowPass` | RB | `19` | `19` | 91 | START | 91 | 98 |

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
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 30 | 14 | inferred_complete_timeline |
| `Action_None` | 31 | 88 | 58 | inferred_complete_timeline |
| `Action_None` | 90 | 180 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 90 | 33 | inferred_complete_timeline |
| `Action_ThrowPass` | 91 | 98 | 8 | inferred_complete_timeline |
| `Action_None` | 99 | 162 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 74 | 58 | inferred_complete_timeline |
| `Action_None` | 77 | 180 | 104 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_RunPostRoute` | 30 | 180 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 83 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 180 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 37 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 41 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_BallSnap` | 17 | 30 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 31 | 78 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 101 | 180 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 36 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 50 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 31 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 40 | 43 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 105 | 89 | inferred_complete_timeline |
| `Action_None` | 114 | 180 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 89 | 73 | inferred_complete_timeline |
| `Action_None` | 96 | 180 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 73 | 57 | inferred_complete_timeline |
| `Action_None` | 91 | 93 | 3 | inferred_complete_timeline |
| `Action_None` | 95 | 180 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 44 | 28 | inferred_complete_timeline |
| `Action_None` | 51 | 65 | 15 | inferred_complete_timeline |
| `Action_None` | 69 | 72 | 4 | inferred_complete_timeline |
| `Action_None` | 74 | 180 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 76 | 60 | inferred_complete_timeline |
| `Action_None` | 81 | 88 | 8 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 114 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 125 | 109 | inferred_complete_timeline |
| `Action_None` | 132 | 180 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 180 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 132 | 116 | inferred_complete_timeline |
| `Action_None` | 134 | 180 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 148 | 132 | inferred_complete_timeline |
| `Action_None` | 158 | 173 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 132 | 116 | inferred_complete_timeline |
| `Action_None` | 136 | 180 | 45 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–83 | 54 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 54–81 | 24 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 87–180 | 94 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 92–104 | 7 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 110–180 | 43 | 6 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 119–180 | 62 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 127–145 | 19 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 132–180 | 49 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 165–166 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [17–30], lower_priority='Action_PassBlock' annotated_start=20, effective_Action_PassBlock_start=31.
- ⚠️ Action 'Action_None' range [17-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-74] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [30-180] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-83] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [88-180] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-132] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-148] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-173] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-89] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-76] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-88] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-44] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-65] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-180] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-132] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-73] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-180] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-88] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-31] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [40-43] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-162] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [31-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [101-180] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-36] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-50] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-24] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-67] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-71] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-83] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-78] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-142] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-175] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-145] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-180] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '30' has 1 frames without a visible bounding box.
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