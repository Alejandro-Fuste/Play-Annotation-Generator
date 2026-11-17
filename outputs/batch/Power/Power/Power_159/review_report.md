# Play-Annotation-Generator Annotation Review — Power_159

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_159`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 63
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ EXACT | `Action_DownBlock` | RB | offense | `19` | `19` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 31 | START | 31 | 258 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 31 | START | 31 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 31 | START | 31 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 31 | START | 31 | 278 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 31 | START | 31 | 394 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 31 | START | 31 | 229 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 31 | START | 31 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 31 | START | 31 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 31 | START | 31 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 31 | START | 31 | 198 |
| ✅ EXACT | `Action_DownBlock` | RB | `19` | `19` | 199 | START | 199 | 250 |
| ✅ EXACT | `Action_DownBlock` | RT | `4` | `4` | 199 | START | 199 | 250 |
| ✅ EXACT | `Action_PullBlock` | LT | `12` | `12` | 199 | START | 199 | 250 |

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
- **Visible Frames:** 31–394
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 394 | 364 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 31–419
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 198 | 168 | inferred_complete_timeline |
| `Action_DownBlock` | 199 | 250 | 52 | inferred_complete_timeline |
| `Action_None` | 251 | 262 | 12 | inferred_complete_timeline |
| `Action_None` | 266 | 419 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 31–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 419 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 31–419
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 228 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 419 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 31–258
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 258 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 31–386
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 198 | 168 | inferred_complete_timeline |
| `Action_PullBlock` | 199 | 250 | 52 | inferred_complete_timeline |
| `Action_None` | 251 | 386 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 31–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 419 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 31–401
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 278 | 248 | inferred_complete_timeline |
| `Action_PreSnap` | 280 | 401 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 31–229
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 229 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 31–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 198 | 168 | inferred_complete_timeline |
| `Action_DownBlock` | 199 | 250 | 52 | inferred_complete_timeline |
| `Action_None` | 251 | 419 | 169 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 31–294
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 268 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 274 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 294 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 31–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 419 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 31–419
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 241 | 211 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 280 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 419 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 31–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 419 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 31–316
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 281 | 251 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 311 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 316 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 31–419
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 215 | 185 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 419 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 31–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 419 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 31–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 419 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 31–414
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 306 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 317 | 414 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 31–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 419 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 31–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 419 | 389 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 31–419 | 380 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 259–262 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 274–291 | 15 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 276–419 | 142 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 288–419 | 132 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 292–419 | 128 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 298–307 | 10 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 310–412 | 101 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 321–326 | 6 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 328–331 | 4 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 331–334 | 4 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 346–347 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 367–372 | 6 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 388–405 | 12 | 3 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 396–419 | 18 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 49 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [31-258] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-228] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-268] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-274] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-294] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-268] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-419] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-280] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-306] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-414] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-419] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-386] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-419] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-215] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-419] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-278] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-401] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-394] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-281] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-311] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-316] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-229] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [199-250] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-262] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-419] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-262] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-283] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-291] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-306] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-347] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-419] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-419] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-419] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-307] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-340] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-412] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-326] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-331] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-334] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-347] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-372] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-395] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-400] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-405] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-401] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-412] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-419] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>