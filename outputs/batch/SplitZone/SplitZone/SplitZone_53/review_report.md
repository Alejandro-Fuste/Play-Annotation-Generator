# Play-Annotation-Generator Annotation Review — SplitZone_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_53`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 100
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `19` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `13` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `17` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 86 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 84 | START | 84 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `15` | 87 | START | 87 | 128 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `16` | `16` | 87 | START | 87 | 161 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `19` | `19` | 87 | START | 87 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `20` | 87 | START | 94 | 142 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 87 | START | 87 | 161 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `13` | `13` | 91 | START | 91 | 161 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 93 | END | 84 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `8` | `8` | 121 | START | 121 | 225 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `19` | `19` | 128 | START | 128 | 161 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 161 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_SnapReceive` | 84 | 93 | 10 | inferred_complete_timeline |
| `Action_None` | 94 | 120 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 121 | 225 | 105 | inferred_complete_timeline |
| `Action_BallCarry` | 235 | 247 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 249 | 255 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 257 | 282 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 120 | 37 | inferred_complete_timeline |
| `Action_None` | 125 | 166 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_SplitBlock` | 91 | 161 | 71 | inferred_complete_timeline |
| `Action_None` | 162 | 224 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 161 | 75 | inferred_complete_timeline |
| `Action_None` | 162 | 299 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 128 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 148 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 161 | 12 | inferred_complete_timeline |
| `Action_None` | 162 | 166 | 5 | inferred_complete_timeline |
| `Action_None` | 168 | 182 | 15 | inferred_complete_timeline |
| `Action_None` | 185 | 230 | 46 | inferred_complete_timeline |
| `Action_None` | 240 | 245 | 6 | inferred_complete_timeline |
| `Action_None` | 248 | 299 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_BallSnap` | 84 | 93 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 142 | 49 | inferred_complete_timeline |
| `Action_ZoneBlock` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 127 | 41 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 128 | 161 | 34 | inferred_complete_timeline |
| `Action_None` | 162 | 299 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 161 | 75 | inferred_complete_timeline |
| `Action_None` | 162 | 181 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 229 | 146 | inferred_complete_timeline |
| `Action_None` | 234 | 276 | 43 | inferred_complete_timeline |
| `Action_None` | 283 | 286 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 174 | 91 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 240 | 60 | inferred_complete_timeline |
| `Action_None` | 243 | 299 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 116 | 33 | inferred_complete_timeline |
| `Action_None` | 126 | 223 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 255 | 172 | inferred_complete_timeline |
| `Action_None` | 257 | 273 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 284 | 201 | inferred_complete_timeline |
| `Action_None` | 286 | 291 | 6 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 150 | 67 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 299 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 288 | 205 | inferred_complete_timeline |
| `Action_None` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 6–166
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 23 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 83 | 44 | inferred_complete_timeline |
| `Action_None` | 84 | 166 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 299 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_None` | 84 | 150 | 67 | inferred_complete_timeline |
| `Action_None` | 158 | 284 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 159–175 | 10 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 160–282 | 107 | 5 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 160–291 | 59 | 14 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 167–299 | 133 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 177–299 | 123 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 204–288 | 62 | 8 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 210–299 | 90 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 227–299 | 73 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 242–244 | 3 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 254–299 | 46 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 280–291 | 10 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 297–299 | 3 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 299–299 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [84–93], lower_priority='Action_ZoneBlock' annotated_start=87, effective_Action_ZoneBlock_start=94.
- ⚠️ Action 'Action_None' range [84-284] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-166] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-229] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-276] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-255] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-273] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [121-225] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-247] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [249-255] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [257-282] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-240] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-284] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-224] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-223] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-148] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-230] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-245] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-288] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [94-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [146-147] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-23] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-215] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-251] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-265] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-182] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-227] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-251] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-268] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-276] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-291] for track '34' has 1 frames without a visible bounding box.
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

</details>