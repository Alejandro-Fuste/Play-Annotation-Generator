# Play-Annotation-Generator Annotation Review — InsideZoneRead_146

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_146`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 115 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 113 | START | 113 | 113 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `15` | `14` | 116 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LG | `9` | `8` | 116 | START | 116 | 185 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 125 | END | 113 | 125 |
| ✅ EXACT | `Action_ReadDefender` | QB | `11` | `10` | 128 | START | 128 | 139 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `10` | 140 | START | 140 | 146 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `16` | `15` | 147 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 185 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–353
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_SnapReceive` | 113 | 125 | 13 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 128 | 139 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 140 | 146 | 7 | inferred_complete_timeline |
| `Action_None` | 147 | 353 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 359 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–351
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 156 | 44 | inferred_complete_timeline |
| `Action_None` | 168 | 346 | 179 | inferred_complete_timeline |
| `Action_None` | 350 | 351 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 279 | 167 | inferred_complete_timeline |
| `Action_None` | 282 | 292 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 185 | 70 | inferred_complete_timeline |
| `Action_None` | 186 | 290 | 105 | inferred_complete_timeline |
| `Action_None` | 295 | 307 | 13 | inferred_complete_timeline |
| `Action_None` | 316 | 320 | 5 | inferred_complete_timeline |
| `Action_None` | 325 | 326 | 2 | inferred_complete_timeline |
| `Action_None` | 335 | 343 | 9 | inferred_complete_timeline |
| `Action_None` | 351 | 352 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 76 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 112 | 34 | inferred_complete_timeline |
| `Action_BallSnap` | 113 | 113 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–18
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 180 | 68 | inferred_complete_timeline |
| `Action_None` | 191 | 232 | 42 | inferred_complete_timeline |
| `Action_None` | 236 | 333 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 163 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 308 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 266 | 154 | inferred_complete_timeline |
| `Action_None` | 268 | 359 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 307 | 195 | inferred_complete_timeline |
| `Action_None` | 309 | 359 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 224 | 112 | inferred_complete_timeline |
| `Action_None` | 226 | 233 | 8 | inferred_complete_timeline |
| `Action_None` | 236 | 245 | 10 | inferred_complete_timeline |
| `Action_None` | 251 | 281 | 31 | inferred_complete_timeline |
| `Action_None` | 283 | 359 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 278 | 166 | inferred_complete_timeline |
| `Action_None` | 280 | 340 | 61 | inferred_complete_timeline |
| `Action_None` | 351 | 352 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 7–15 | 9 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 136–359 | 185 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 140–145 | 6 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 149–166 | 18 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 171–353 | 84 | 7 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 176–359 | 183 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 192–193 | 2 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 193–359 | 167 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 199–340 | 132 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 199–233 | 35 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 199–353 | 155 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 200–359 | 96 | 6 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 212–214 | 3 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 231–359 | 85 | 3 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 238–326 | 79 | 5 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 253–359 | 103 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 295–316 | 13 | 3 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 299–359 | 57 | 4 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 352–354 | 3 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 355–356 | 2 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 359–359 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `15` (C)
- ❌ Missing segment for action `Action_BallCarry` on target `16` (Position_Unknown)

### Track Identity Issues

- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 291: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 291: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '14' has invalid range: start=116, end=113. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '15' has invalid range: start=147, end=15. Clamping end to start.
- ⚠️ Action 'Action_None' range [113-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-346] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-307] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-359] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-224] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-233] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-245] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-281] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-266] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-279] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-292] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-232] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-333] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-278] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-340] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-290] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-307] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-320] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-343] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-308] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-353] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-163] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' for track '14' starts at frame 113, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallSnap' range [113-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-15] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-160] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-221] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-259] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-353] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-226] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-317] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-340] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-233] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-353] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-213] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-252] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-314] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-252] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-359] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-296] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-305] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-340] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-300] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-307] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-314] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-324] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-331] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-359] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-354] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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