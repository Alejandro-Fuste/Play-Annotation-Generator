# Play-Annotation-Generator Annotation Review — Counter_283

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_283`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ✅ EXACT | `Action_DownBlock` | DT | defense | `21` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `23` | `21` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `20` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `12` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 9 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 17 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `23` | `Group` | 0 | START | 28 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 62 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 60 | START | 60 | 78 |
| ✅ EXACT | `Action_DownBlock` | DT | `21` | `19` | 63 | START | 63 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `23` | `21` | 63 | START | 63 | 93 |
| ✅ EXACT | `Action_PullBlock` | RG | `20` | `18` | 63 | START | 63 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `6` | `5` | 63 | START | 63 | 116 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 78 | END | 60 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `11` | `10` | 90 | START | 90 | 96 |
| ✅ EXACT | `Action_BallCarry` | RB | `10` | `9` | 106 | START | 106 | 293 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 150 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_SnapReceive` | 60 | 78 | 19 | inferred_complete_timeline |
| `Action_None` | 79 | 89 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 90 | 96 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 98 | 105 | 8 | inferred_complete_timeline |
| `Action_None` | 106 | 299 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 293 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 279 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 149 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 291 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 63 | 116 | 54 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 140 | 150 | 11 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 87 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 28–119
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 62 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 63 | 93 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 115 | 119 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 9–154
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 59 | 51 | inferred_complete_timeline |
| `Action_BallSnap` | 60 | 78 | 19 | inferred_complete_timeline |
| `Action_None` | 79 | 84 | 6 | inferred_complete_timeline |
| `Action_None` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_None` | 95 | 138 | 44 | inferred_complete_timeline |
| `Action_None` | 144 | 154 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 17–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 17 | 62 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 63 | 150 | 88 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–290
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 59 | 42 | inferred_complete_timeline |
| `Action_None` | 60 | 290 | 231 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 299 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `24`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `24`
- **team_side:** `defense`
- **Visible Frames:** 29–183
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 59 | 31 | inferred_complete_timeline |
| `Action_None` | 60 | 97 | 38 | inferred_complete_timeline |
| `Action_None` | 154 | 163 | 10 | inferred_complete_timeline |
| `Action_None` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_None` | 176 | 183 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `21`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 21–115
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 62 | 42 | inferred_complete_timeline |
| `Action_DownBlock` | 63 | 115 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 122 | 63 | inferred_complete_timeline |
| `Action_None` | 135 | 154 | 20 | inferred_complete_timeline |
| `Action_None` | 156 | 222 | 67 | inferred_complete_timeline |
| `Action_None` | 226 | 299 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 145 | 86 | inferred_complete_timeline |
| `Action_None` | 150 | 157 | 8 | inferred_complete_timeline |
| `Action_None` | 174 | 195 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 293 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–291
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 291 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 134 | 75 | inferred_complete_timeline |
| `Action_None` | 142 | 151 | 10 | inferred_complete_timeline |
| `Action_None` | 160 | 164 | 5 | inferred_complete_timeline |
| `Action_None` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_None` | 201 | 203 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 212 | 153 | inferred_complete_timeline |
| `Action_None` | 216 | 299 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 299 | 240 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–299 | 285 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 26–39 | 14 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 90–299 | 209 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 166–299 | 133 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 180–299 | 120 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 183–299 | 117 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 188–291 | 102 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 204–299 | 96 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 229–293 | 65 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 251–256 | 6 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 262–293 | 32 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 264–268 | 5 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 274–275 | 2 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 286–287 | 2 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 292–297 | 6 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 295–296 | 2 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `23` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 58 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [60-279] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-122] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-154] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-222] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-293] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-291] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [63-116] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-212] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-299] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-151] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-164] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-291] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-293] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [90-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-87] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-146] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-171] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-157] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-195] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-59] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-290] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-138] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [63-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-39] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [63-93] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [115-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-97] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-163] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-266] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-196] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-246] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-291] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-293] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-293] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-297] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>