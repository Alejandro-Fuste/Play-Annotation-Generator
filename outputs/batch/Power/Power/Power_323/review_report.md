# Play-Annotation-Generator Annotation Review — Power_323

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_323`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 194
- **Validation Warnings:** 228
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 167
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `18` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `1` | `Group` | 13 | START | 13 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 13 | START | 13 | 89 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 13 | START | 13 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 13 | START | 13 | 262 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `5` | `Group` | 13 | START | 13 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 13 | START | 13 | 108 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `10` | `10` | 90 | START | 90 | 132 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `14` | `14` | 90 | START | 90 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `21` | `20` | 90 | START | 90 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `18` | `17` | 90 | START | 90 | 117 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 13–262
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 262 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 13–237
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 118 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 158 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 211 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 237 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 13–299
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 108 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 114 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 129 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 158 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 299 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 13–118
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 109 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 118 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 13–161
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 148 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 161 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 13–299
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 89 | 77 | inferred_complete_timeline |
| `Action_DownBlock` | 90 | 100 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 126 | 130 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 132 | 1 | inferred_complete_timeline |
| `Action_None` | 133 | 133 | 1 | inferred_complete_timeline |
| `Action_None` | 144 | 203 | 60 | inferred_complete_timeline |
| `Action_None` | 206 | 208 | 3 | inferred_complete_timeline |
| `Action_None` | 210 | 299 | 90 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 13–299
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 22 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 109 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 117 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 133 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 158 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 194 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 299 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 13–195
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 109 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 117 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 166 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 195 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 13–115
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 20 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 107 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 115 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 19–299
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 22 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 109 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 118 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 164 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 299 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 13–297
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 22 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 109 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 141 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 158 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 194 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 232 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 236 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 276 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 289 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 297 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 13–299
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 20 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 109 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 117 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 158 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 194 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 236 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 243 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 249 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 254 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 299 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 13–265
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 255 | 243 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 265 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 13–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 252 | 240 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 263 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 299 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 13–253
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 144 | 132 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 161 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 214 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 253 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–298
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 25 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 298 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 13–241
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 121 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 133 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 166 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 195 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 208 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 214 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 219 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 232 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 237 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 241 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 13–299 | 285 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 13–243 | 209 | 9 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 13–299 | 274 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 13–262 | 171 | 13 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 15–299 | 232 | 12 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 27–30 | 4 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 127–163 | 17 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 127–299 | 91 | 5 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 169–299 | 131 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 175–188 | 12 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 179–296 | 55 | 8 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 185–194 | 9 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 191–289 | 32 | 8 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 230–299 | 66 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 263–297 | 28 | 4 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 269–297 | 28 | 2 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 274–299 | 26 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 276–293 | 18 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 278–297 | 19 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 280–299 | 20 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 287–297 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 181 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 646: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ Row 646: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 646: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 646: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [13-22] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-109] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-133] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-163] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-194] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-202] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-232] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-241] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-276] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-289] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-297] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-148] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-161] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-255] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-181] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-144] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-161] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-253] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-158] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-211] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-237] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-25] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-298] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-252] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-263] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-22] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-117] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-158] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-194] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-299] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-158] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-163] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-181] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-243] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-258] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-265] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-109] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-166] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-195] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-121] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-133] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-171] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-214] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-219] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-232] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-241] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [90-100] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [102-107] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [126-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 133, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [133-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-109] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-117] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-158] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-194] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-236] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-243] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-249] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-254] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [90-117] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [126-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 133, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [133-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-158] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-194] for track '17' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-236] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-262] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-20] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-18] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [90-108] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [112-117] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [126-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '20' starts at frame 133, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [133-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-158] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-263] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-22] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-109] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-118] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-164] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-30] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-133] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-163] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-181] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-188] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-181] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-188] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-194] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-241] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-271] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-290] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-296] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-186] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-194] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-193] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-196] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-207] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-254] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-271] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-289] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-299] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-264] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-290] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-297] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-297] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-299] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-293] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-290] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-297] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-299] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-290] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-297] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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