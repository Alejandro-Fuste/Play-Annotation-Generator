# Play-Annotation-Generator Annotation Review — DeepCross_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `DeepCross_13`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_DeepCross`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 114
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
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 8 | START | 8 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `11` | `11` | 11 | START | 21 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `12` | `12` | 11 | START | 11 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 11 | START | 11 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 11 | START | 11 | 46 |
| ✅ EXACT | `Action_PassBlock` | LT | `20` | `20` | 11 | START | 11 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunDeepCrossRoute` | WR2 | `1` | `1` | 20 | START | 20 | 92 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 20 | END | 8 | 20 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 116 | START | 116 | 124 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 20 | 13 | inferred_complete_timeline |
| `Action_None` | 21 | 115 | 95 | inferred_complete_timeline |
| `Action_ThrowPass` | 116 | 124 | 9 | inferred_complete_timeline |
| `Action_None` | 125 | 157 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 57 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 64 | 57 | inferred_complete_timeline |
| `Action_None` | 69 | 101 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 20 | 92 | 73 | inferred_complete_timeline |
| `Action_RunDeepCrossRoute` | 94 | 190 | 97 | inferred_complete_timeline |
| `Action_None` | 191 | 202 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 39 | 32 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_None` | 51 | 210 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 115 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 26 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 32 | 41 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 169 | 121 | inferred_complete_timeline |
| `Action_PassBlock` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 188 | 208 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 20 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 63 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 106 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 163 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 46 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 58 | 62 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 64 | 74 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 148 | 149 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 58 | 48 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 87 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 106 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 169 | 162 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 169 | 162 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |
| `Action_None` | 179 | 210 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–197
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 107 | 100 | inferred_complete_timeline |
| `Action_None` | 109 | 156 | 48 | inferred_complete_timeline |
| `Action_None` | 159 | 165 | 7 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 96 | 136 | 41 | inferred_complete_timeline |
| `Action_None` | 139 | 155 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 59 | 52 | inferred_complete_timeline |
| `Action_None` | 62 | 69 | 8 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 210 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 147 | 140 | inferred_complete_timeline |
| `Action_None` | 149 | 210 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 169 | 162 | inferred_complete_timeline |
| `Action_None` | 177 | 179 | 3 | inferred_complete_timeline |
| `Action_None` | 182 | 201 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 26–27 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 29–158 | 58 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 68–163 | 95 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 74–164 | 91 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 83–94 | 12 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 93–94 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 95–196 | 93 | 5 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 102–206 | 66 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 110–147 | 38 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 125–128 | 4 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 186–210 | 24 | 2 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 199–200 | 2 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 199–210 | 12 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunDeepCrossRoute` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [8–20], lower_priority='Action_PassBlock' annotated_start=11, effective_Action_PassBlock_start=21.
- ⚠️ Action 'Action_None' range [8-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [20-92] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunDeepCrossRoute' range [94-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-202] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-39] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-169] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-59] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-69] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-64] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-101] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-201] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-136] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-147] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-63] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [111-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [116-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-163] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-87] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-157] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-107] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-26] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-29] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [32-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-169] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [179-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [188-208] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-46] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [58-62] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [64-74] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [148-149] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-169] for track '19' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-27] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-31] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-49] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-82] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-163] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-164] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-94] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-157] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-168] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-158] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-206] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-147] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '37' has 1 frames without a visible bounding box.
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

</details>