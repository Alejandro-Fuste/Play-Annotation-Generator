# Play-Annotation-Generator Annotation Review — Slants0to10_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_49`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 4 | START | 4 | 19 |
| ✅ EXACT | `Action_PassBlock` | LT | `10` | `10` | 7 | START | 7 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 7 | START | 7 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 7 | START | 20 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 7 | START | 7 | 10 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `5` | `5` | 7 | START | 7 | 68 |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | `2` | `2` | 19 | START | 19 | 66 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 19 | END | 4 | 19 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 58 | START | 58 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `2` | `2` | 88 | START | 88 | 108 |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 4 | 19 | 16 | inferred_complete_timeline |
| `Action_None` | 20 | 57 | 38 | inferred_complete_timeline |
| `Action_ThrowPass` | 58 | 66 | 9 | inferred_complete_timeline |
| `Action_None` | 67 | 85 | 19 | inferred_complete_timeline |
| `Action_None` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 210 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 19 | 66 | 48 | inferred_complete_timeline |
| `Action_None` | 67 | 87 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 108 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 113 | 124 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 127 | 203 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 103 | 100 | inferred_complete_timeline |
| `Action_None` | 108 | 113 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 23 | 20 | inferred_complete_timeline |
| `Action_None` | 25 | 149 | 125 | inferred_complete_timeline |
| `Action_None` | 154 | 210 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 151 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 210 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 68 | 62 | inferred_complete_timeline |
| `Action_PassBlock` | 90 | 173 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 4 | 19 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 34 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 39 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 46 | 71 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 77 | 78 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–49
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 10 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 49 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 56 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 68 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 210 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 59 | 56 | inferred_complete_timeline |
| `Action_None` | 65 | 74 | 10 | inferred_complete_timeline |
| `Action_None` | 79 | 103 | 25 | inferred_complete_timeline |
| `Action_None` | 105 | 113 | 9 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 192 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 64 | 61 | inferred_complete_timeline |
| `Action_None` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_None` | 79 | 210 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 86 | 83 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_None` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 110 | 210 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 101 | 98 | inferred_complete_timeline |
| `Action_None` | 103 | 113 | 11 | inferred_complete_timeline |
| `Action_None` | 116 | 145 | 30 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 189 | 29 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 133 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 202 | 199 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `27` | Position_Unknown | Team_Unknown | 43–53 | 11 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 102–210 | 97 | 4 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 120–125 | 6 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 132–210 | 79 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 161–205 | 41 | 3 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 175–176 | 2 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 197–210 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [4–19], lower_priority='Action_PassBlock' annotated_start=7, effective_Action_PassBlock_start=20.
- ⚠️ Action 'Action_None' range [4-59] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-74] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-113] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-192] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-133] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [113-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [127-203] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-113] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-101] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-113] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-145] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-189] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-68] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [90-173] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-64] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-73] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-202] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-210] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-86] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-85] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-23] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-149] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-56] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-68] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-34] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-39] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [46-71] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-75] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [77-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '21' starts at frame 7, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [7-10] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-44] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-49] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-162] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-172] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '28' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>