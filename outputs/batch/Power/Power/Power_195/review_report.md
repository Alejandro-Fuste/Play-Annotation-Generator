# Play-Annotation-Generator Annotation Review — Power_195

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_195`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 62
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `21` | `21` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 18 | START | 18 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 18 | START | 18 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 18 | START | 18 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `2` | `Group` | 18 | START | 18 | 245 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 18 | START | 18 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 18 | START | 18 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 18 | START | 18 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 18 | START | 18 | 299 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 18 | START | 18 | 168 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `15` | `15` | 100 | START | 100 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `18` | `18` | 100 | START | 100 | 139 |
| ✅ EXACT | `Action_DownBlock` | LT | `21` | `21` | 100 | START | 100 | 181 |
| ✅ EXACT | `Action_PullBlock` | RG | `20` | `20` | 100 | START | 100 | 181 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 18–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 299 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 18–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 245 | 228 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 262 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 264 | 299 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 18–234
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 215 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 234 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 18–299
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 168 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 299 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 18–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 99 | 82 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 181 | 82 | inferred_complete_timeline |
| `Action_None` | 182 | 299 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 18–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 99 | 82 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 139 | 40 | inferred_complete_timeline |
| `Action_DownBlock` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 146 | 181 | 36 | inferred_complete_timeline |
| `Action_None` | 182 | 299 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 18–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 99 | 82 | inferred_complete_timeline |
| `Action_DownBlock` | 100 | 111 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 122 | 181 | 60 | inferred_complete_timeline |
| `Action_None` | 182 | 299 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 18–272
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 99 | 82 | inferred_complete_timeline |
| `Action_PullBlock` | 100 | 181 | 82 | inferred_complete_timeline |
| `Action_None` | 182 | 220 | 39 | inferred_complete_timeline |
| `Action_None` | 222 | 224 | 3 | inferred_complete_timeline |
| `Action_None` | 237 | 272 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 18–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 299 | 282 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 18–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 135 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 299 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 18–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 122 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 299 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 18–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 299 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 18–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 129 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 299 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 18–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 160 | 143 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 299 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 18–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 247 | 230 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 250 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 255 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 299 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 18–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 299 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 18–244
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 240 | 223 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 244 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 18–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 185 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 280 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 299 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 18–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 215 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 299 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 18–299 | 282 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 18–299 | 281 | 2 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 18–294 | 277 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 175–192 | 18 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 243–287 | 30 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 246–299 | 54 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 266–299 | 34 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 292–297 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 36 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 392: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ Row 392: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 392: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [18-185] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-245] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-262] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-294] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-215] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-234] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-122] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-168] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-185] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-280] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-240] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-244] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-215] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-247] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-250] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-255] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [100-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [100-139] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [143-144] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-220] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-272] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-221] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-249] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-256] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-267] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-287] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-297] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>