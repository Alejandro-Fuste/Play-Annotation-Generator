# Play-Annotation-Generator Annotation Review — SlantAndGo_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_7`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 110
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `5` |
| ✅ EXACT | `Action_SellRoute` | WR2 | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR2 | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 14 | START | 14 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `16` | `16` | 19 | START | 19 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `17` | 19 | START | 19 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 19 | START | 19 | 95 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `20` | `20` | 19 | START | 41 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 19 | START | 19 | 131 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `5` | 30 | END | 14 | 30 |
| ✅ EXACT | `Action_SellRoute` | WR2 | `7` | `7` | 50 | START | 50 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR2 | `7` | `7` | 69 | START | 69 | 78 |
| ✅ EXACT | `Action_ThrowPass` | QB | `5` | `5` | 96 | START | 96 | 104 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_SnapReceive` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_None` | 31 | 95 | 65 | inferred_complete_timeline |
| `Action_ThrowPass` | 96 | 104 | 9 | inferred_complete_timeline |
| `Action_None` | 105 | 110 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_SellRoute` | 50 | 68 | 19 | inferred_complete_timeline |
| `Action_VerticalStem` | 69 | 78 | 10 | inferred_complete_timeline |
| `Action_VerticalStem` | 82 | 129 | 48 | inferred_complete_timeline |
| `Action_VerticalStem` | 138 | 164 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 161 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 200 | 187 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 66 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 104 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 106 | 111 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 127 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 161 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 173 | 174 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 65 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 119 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 145 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 163 | 165 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_BallSnap` | 14 | 19 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 156 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 131 | 113 | inferred_complete_timeline |
| `Action_PassBlock` | 135 | 139 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 19 | 95 | 77 | inferred_complete_timeline |
| `Action_PassBlock` | 97 | 100 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 124 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 143 | 148 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 150 | 181 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 59 | 46 | inferred_complete_timeline |
| `Action_None` | 62 | 135 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 73 | 60 | inferred_complete_timeline |
| `Action_None` | 78 | 87 | 10 | inferred_complete_timeline |
| `Action_None` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_None` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 107 | 94 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 136 | 155 | 20 | inferred_complete_timeline |
| `Action_None` | 165 | 169 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 80 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 91 | 78 | inferred_complete_timeline |
| `Action_None` | 94 | 140 | 47 | inferred_complete_timeline |
| `Action_None` | 145 | 149 | 5 | inferred_complete_timeline |
| `Action_None` | 151 | 210 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 76 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 164 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 210 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 126 | 113 | inferred_complete_timeline |
| `Action_None` | 130 | 161 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 104 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 92 | 79 | inferred_complete_timeline |
| `Action_None` | 94 | 101 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 20 | 7 | inferred_complete_timeline |
| `Action_None` | 23 | 26 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–161 | 160 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 16–27 | 5 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 24–29 | 6 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 25–164 | 105 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 81–159 | 10 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 84–173 | 61 | 5 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 92–166 | 58 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 113–172 | 17 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 120–122 | 3 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 137–163 | 22 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 158–210 | 53 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (5 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `20` (C): Annotated start 19 != Inferred start 41
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 84 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 12: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 12: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [14–30], lower_priority='Action_PassBlock' annotated_start=19, effective_Action_PassBlock_start=31.
- ⚠️ Action 'Action_None' range [14-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-92] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-101] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-161] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-164] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-87] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-20] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-26] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [69-78] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [82-129] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [138-164] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-91] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-140] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-200] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-104] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-126] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-76] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-80] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-66] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-104] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [106-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-161] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [173-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-65] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-123] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [126-128] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-145] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [163-165] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-107] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-95] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [97-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [143-148] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [150-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [14-19] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-156] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [19-131] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [135-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-17] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-27] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-29] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-114] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-90] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-156] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-128] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-152] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-160] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-163] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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