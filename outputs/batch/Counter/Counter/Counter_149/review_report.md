# Play-Annotation-Generator Annotation Review — Counter_149

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_149`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_DownBlock` | TE | offense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `17` | `16` |
| ✅ EXACT | `Action_DownBlock` | LB2 | defense | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | TE | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | LG | `14` | `13` | 122 | START | 122 | 134 |
| ✅ EXACT | `Action_DownBlock` | TE | `15` | `14` | 125 | START | 125 | 140 |
| ✅ EXACT | `Action_DownBlock` | LT | `17` | `16` | 125 | START | 125 | 190 |
| ✅ EXACT | `Action_DownBlock` | LB2 | `4` | `3` | 125 | START | 125 | 190 |
| ✅ EXACT | `Action_PullBlock` | RG | `21` | `20` | 125 | START | 125 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `9` | `8` | 125 | START | 125 | 170 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 137 | END | 122 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | TE | `15` | `14` | 141 | START | 141 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `12` | `11` | 166 | START | 166 | 182 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 190 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–269
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_SnapReceive` | 122 | 137 | 16 | inferred_complete_timeline |
| `Action_None` | 138 | 184 | 47 | inferred_complete_timeline |
| `Action_None` | 194 | 269 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_BallCarry` | 166 | 182 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 186 | 210 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 216 | 228 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 231 | 234 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 236 | 269 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 269 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 269 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 140 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 146 | 165 | 20 | inferred_complete_timeline |
| `Action_None` | 166 | 269 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 190 | 66 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_BallSnap` | 122 | 134 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_None` | 138 | 144 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–211
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PullBlock` | 125 | 190 | 66 | inferred_complete_timeline |
| `Action_None` | 191 | 211 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 125 | 170 | 46 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 182 | 186 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 139 | 18 | inferred_complete_timeline |
| `Action_None` | 142 | 156 | 15 | inferred_complete_timeline |
| `Action_None` | 175 | 193 | 19 | inferred_complete_timeline |
| `Action_None` | 195 | 262 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 236 | 115 | inferred_complete_timeline |
| `Action_None` | 239 | 240 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_None` | 256 | 269 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 140 | 19 | inferred_complete_timeline |
| `Action_None` | 144 | 157 | 14 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 168 | 269 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 236 | 115 | inferred_complete_timeline |
| `Action_None` | 238 | 269 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 161 | 40 | inferred_complete_timeline |
| `Action_None` | 163 | 171 | 9 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_DownBlock` | 125 | 190 | 66 | inferred_complete_timeline |
| `Action_None` | 191 | 215 | 25 | inferred_complete_timeline |
| `Action_None` | 217 | 269 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 176 | 55 | inferred_complete_timeline |
| `Action_None` | 180 | 198 | 19 | inferred_complete_timeline |
| `Action_None` | 200 | 256 | 57 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 215 | 94 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 269 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 219 | 98 | inferred_complete_timeline |
| `Action_None` | 222 | 269 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 212 | 91 | inferred_complete_timeline |
| `Action_None` | 214 | 224 | 11 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_None` | 122 | 236 | 115 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–269 | 269 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 26–269 | 237 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 168–245 | 48 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 175–269 | 95 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 199–269 | 60 | 4 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 232–269 | 37 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 258–267 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 300: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [122-263] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-215] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-269] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-236] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-236] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [125-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [182-186] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-176] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-256] for track '9' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-215] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [166-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [186-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-214] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [216-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [231-234] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-236] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [122-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-144] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [141-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [146-165] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-184] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [125-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-193] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-262] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-157] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-212] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-224] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-128] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-187] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-215] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-204] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-250] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-263] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>