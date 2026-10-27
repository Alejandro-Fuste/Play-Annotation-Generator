# Play-Annotation-Generator Annotation Review — Counter_335

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_335`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 78
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
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `9` | `8` |
| ⚠️ START CHANGED | `Action_PullBlock` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 28 | START | 28 | 41 |
| ✅ EXACT | `Action_DownBlock` | LG | `21` | `20` | 31 | START | 31 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `4` | `3` | 31 | START | 31 | 63 |
| ✅ EXACT | `Action_DownBlock` | RG | `9` | `8` | 31 | START | 31 | 68 |
| ⚠️ START CHANGED | `Action_PullBlock` | C | `22` | `21` | 31 | START | 42 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `15` | `14` | 31 | START | 31 | 78 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 41 | END | 28 | 41 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 61 | START | 61 | 88 |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `9` | 89 | START | 89 | 180 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 127 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_SnapReceive` | 28 | 41 | 14 | inferred_complete_timeline |
| `Action_None` | 42 | 60 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 61 | 88 | 28 | inferred_complete_timeline |
| `Action_None` | 89 | 101 | 13 | inferred_complete_timeline |
| `Action_None` | 111 | 114 | 4 | inferred_complete_timeline |
| `Action_None` | 119 | 121 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 88 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 89 | 180 | 92 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 180 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 180 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 180 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 180 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 31 | 63 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 83 | 103 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 105 | 125 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 31 | 57 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_BallSnap` | 28 | 41 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 42 | 127 | 86 | inferred_complete_timeline |
| `Action_None` | 128 | 180 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 31 | 68 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 31 | 78 | 48 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 137 | 110 | inferred_complete_timeline |
| `Action_None` | 139 | 148 | 10 | inferred_complete_timeline |
| `Action_None` | 150 | 166 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 53 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 59 | 32 | inferred_complete_timeline |
| `Action_None` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_None` | 71 | 103 | 33 | inferred_complete_timeline |
| `Action_None` | 105 | 122 | 18 | inferred_complete_timeline |
| `Action_None` | 127 | 180 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 45 | 18 | inferred_complete_timeline |
| `Action_None` | 74 | 131 | 58 | inferred_complete_timeline |
| `Action_None` | 133 | 180 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 180 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 137 | 110 | inferred_complete_timeline |
| `Action_None` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 180 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 129 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 180 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 156 | 129 | inferred_complete_timeline |
| `Action_None` | 158 | 180 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 180 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_None` | 28 | 180 | 153 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 88–180 | 88 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 115–180 | 66 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 126–176 | 51 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 138–174 | 35 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 140–180 | 41 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 151–180 | 29 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 160–173 | 11 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (4 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `22` (C): Annotated start 31 != Inferred start 42
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (LT) duration 95 frames exceeds threshold 90 frames [start=31, end=125].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '21' (C) duration 97 frames exceeds threshold 90 frames [start=31, end=127].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [28–41], lower_priority='Action_PullBlock' annotated_start=31, effective_Action_PullBlock_start=42.
- ⚠️ Action 'Action_None' range [28-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [31-63] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [66-67] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [83-103] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [105-125] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-180] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-137] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-180] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [31-68] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [89-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-137] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-148] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-166] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-156] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [31-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [112-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-180] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-53] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-45] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [31-57] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [42-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-176] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-150] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-174] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-176] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-166] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '30' has 1 frames without a visible bounding box.
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