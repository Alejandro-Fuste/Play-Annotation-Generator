# Play-Annotation-Generator Annotation Review — CrackToss_65

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_65`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | CB2 | defense | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 3 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 3 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 3 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 0 | START | 3 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 3 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 3 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 3 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 3 | 57 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 58 | START | 58 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | CB2 | `3` | `2` | 61 | START | 61 | 86 |
| ✅ EXACT | `Action_PullBlock` | RT | `14` | `13` | 61 | START | 61 | 112 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 66 | END | 58 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `16` | `15` | 70 | START | 70 | 123 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 112 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 3–145
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 66 | 9 | inferred_complete_timeline |
| `Action_None` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 123 | 54 | inferred_complete_timeline |
| `Action_BallCarry` | 131 | 137 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 145 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 3–175
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 141 | 84 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 3–175
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 175 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 3–137
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 108 | 51 | inferred_complete_timeline |
| `Action_None` | 110 | 115 | 6 | inferred_complete_timeline |
| `Action_None` | 120 | 137 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 3–100
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 100 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 3–124
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_BallSnap` | 58 | 66 | 9 | inferred_complete_timeline |
| `Action_None` | 67 | 114 | 48 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 3–90
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 75 | 18 | inferred_complete_timeline |
| `Action_None` | 81 | 83 | 3 | inferred_complete_timeline |
| `Action_None` | 87 | 90 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 3–161
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 60 | 58 | inferred_complete_timeline |
| `Action_PullBlock` | 61 | 112 | 52 | inferred_complete_timeline |
| `Action_None` | 113 | 129 | 17 | inferred_complete_timeline |
| `Action_None` | 156 | 161 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 3–149
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 104 | 47 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 112 | 116 | 5 | inferred_complete_timeline |
| `Action_None` | 120 | 125 | 6 | inferred_complete_timeline |
| `Action_None` | 130 | 149 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 3–153
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 121 | 64 | inferred_complete_timeline |
| `Action_None` | 136 | 153 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–175
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 69 | 12 | inferred_complete_timeline |
| `Action_None` | 73 | 161 | 89 | inferred_complete_timeline |
| `Action_None` | 171 | 175 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–161
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 154 | 97 | inferred_complete_timeline |
| `Action_None` | 157 | 161 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–175
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 131 | 74 | inferred_complete_timeline |
| `Action_None` | 133 | 145 | 13 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 175 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–175
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 107 | 50 | inferred_complete_timeline |
| `Action_None` | 122 | 175 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–175
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 175 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 3–112
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 60 | 58 | inferred_complete_timeline |
| `Action_CrackBlock` | 61 | 86 | 26 | inferred_complete_timeline |
| `Action_CrackBlock` | 99 | 112 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 3–114
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 114 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 3–119
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 116 | 59 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 3–131
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 57 | 55 | inferred_complete_timeline |
| `Action_None` | 58 | 131 | 74 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 3–131 | 129 | 2 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 3–175 | 173 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 3–127 | 122 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 90–175 | 54 | 5 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 113–175 | 39 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 119–128 | 8 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 138–175 | 38 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 141–175 | 22 | 3 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 163–175 | 13 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 164–165 | 2 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 167–175 | 9 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 132: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ Row 132: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [58-131] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-104] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-149] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [61-86] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [99-112] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-175] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-131] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-69] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-161] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-108] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-137] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-141] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-175] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-75] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-154] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-175] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-129] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-106] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-123] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [131-137] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-175] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-100] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-114] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-153] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-127] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-151] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-175] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-154] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>