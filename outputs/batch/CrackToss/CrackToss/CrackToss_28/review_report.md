# Play-Annotation-Generator Annotation Review — CrackToss_28

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_28`
- **Frame Range:** 0 to 298 (299 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 298
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 54
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_CrackBlock` | WR1 | offense | `13` | `12` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Toss` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 168 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 126 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `6` | `5` | 124 | START | N/A | N/A |
| ✅ EXACT | `Action_CrackBlock` | WR1 | `13` | `12` | 127 | START | 127 | 211 |
| ✅ EXACT | `Action_PullBlock` | LT | `9` | `8` | 127 | START | 127 | 163 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 130 | END | 124 | 130 |
| ✅ EXACT | `Action_Toss` | QB | `15` | `14` | 152 | START | 152 | 168 |
| ✅ EXACT | `Action_BallCarry` | RB | `11` | `10` | 169 | START | 169 | 298 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 211 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_SnapReceive` | 124 | 130 | 7 | inferred_complete_timeline |
| `Action_None` | 131 | 151 | 21 | inferred_complete_timeline |
| `Action_Toss` | 152 | 168 | 17 | inferred_complete_timeline |
| `Action_None` | 169 | 194 | 26 | inferred_complete_timeline |
| `Action_None` | 198 | 269 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_BallCarry` | 169 | 298 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 35 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 79 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 126 | 41 | inferred_complete_timeline |
| `Action_CrackBlock` | 127 | 211 | 85 | inferred_complete_timeline |
| `Action_None` | 212 | 233 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 146 | 23 | inferred_complete_timeline |
| `Action_None` | 152 | 181 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 214 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PullBlock` | 127 | 163 | 37 | inferred_complete_timeline |
| `Action_None` | 214 | 219 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 188 | 65 | inferred_complete_timeline |
| `Action_None` | 194 | 239 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 136 | 13 | inferred_complete_timeline |
| `Action_None` | 157 | 234 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 154 | 31 | inferred_complete_timeline |
| `Action_None` | 176 | 209 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 123 | 77 | inferred_complete_timeline |
| `Action_None` | 124 | 183 | 60 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 219 | 32 | inferred_complete_timeline |
| `Action_None` | 226 | 230 | 5 | inferred_complete_timeline |
| `Action_None` | 235 | 260 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 184 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 166 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 157 | 34 | inferred_complete_timeline |
| `Action_None` | 159 | 173 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 213 | 90 | inferred_complete_timeline |
| `Action_None` | 219 | 266 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 123 | 18 | inferred_complete_timeline |
| `Action_None` | 124 | 231 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_None` | 124 | 181 | 58 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 13–298 | 278 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 40–147 | 108 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 99–205 | 104 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 143–298 | 156 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 166–298 | 113 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 174–243 | 70 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 188–282 | 77 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 190–289 | 97 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 196–298 | 103 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 197–298 | 102 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 296–298 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `6` (C)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '5' has invalid range: start=124, end=33. Clamping end to start.
- ⚠️ Action 'Action_None' range [124-184] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-123] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-183] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-260] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-166] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-157] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-173] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-214] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-266] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-209] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [127-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-219] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-181] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-298] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-123] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-231] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-35] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-79] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [127-211] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-233] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-194] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-136] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-123] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-161] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-298] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-205] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-258] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-281] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-243] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-245] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-282] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-239] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-250] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-289] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.

</details>