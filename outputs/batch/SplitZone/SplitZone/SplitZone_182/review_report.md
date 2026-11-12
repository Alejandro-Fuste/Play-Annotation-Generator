# Play-Annotation-Generator Annotation Review — SplitZone_182

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_182`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 161
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB1 | defense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `10` | `10` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 9 | START | 10 | 167 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 9 | START | 10 | 175 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 9 | START | 10 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 9 | START | 10 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 9 | START | 72 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 9 | START | 10 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 9 | START | 10 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 9 | START | 10 | 165 |
| ✅ EXACT | `Action_BallSnap` | LB1 | `7` | `7` | 163 | START | 163 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `13` | `13` | 166 | START | 166 | 182 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 166 | START | 169 | 177 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 166 | START | 166 | 178 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `6` | `6` | 166 | START | 166 | 219 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `9` | 166 | START | 166 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `10` | `10` | 168 | START | 168 | 169 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `12` | `12` | 175 | END | 169 | 171 |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | `12` | `12` | 181 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `11` | 191 | START | 224 | 239 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 274 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 10–171
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 13 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 25 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 134 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 169 | 171 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 10–243
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 175 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 224 | 239 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 242 | 243 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 10–234
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 167 | 158 | inferred_complete_timeline |
| `Action_SplitBlock` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_SplitBlock` | 174 | 234 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 10–178
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 165 | 156 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 178 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 10–257
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 165 | 156 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 198 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 200 | 210 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 217 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 253 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 256 | 257 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 72–213
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 72 | 76 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 86 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 90 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 169 | 177 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 188 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 200 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 213 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 10–219
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 56 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 165 | 107 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 219 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 10–263
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 165 | 156 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 182 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 208 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 219 | 245 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 247 | 249 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 251 | 263 | 13 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 10–247
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 162 | 153 | inferred_complete_timeline |
| `Action_None` | 163 | 247 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 10–395
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 162 | 153 | inferred_complete_timeline |
| `Action_None` | 163 | 395 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 10–255
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 162 | 153 | inferred_complete_timeline |
| `Action_None` | 163 | 255 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 10–41
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 41 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 10–241
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 162 | 153 | inferred_complete_timeline |
| `Action_BallSnap` | 163 | 175 | 13 | inferred_complete_timeline |
| `Action_None` | 176 | 241 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 10–272
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 162 | 153 | inferred_complete_timeline |
| `Action_None` | 163 | 190 | 28 | inferred_complete_timeline |
| `Action_None` | 195 | 215 | 21 | inferred_complete_timeline |
| `Action_None` | 226 | 232 | 7 | inferred_complete_timeline |
| `Action_None` | 247 | 250 | 4 | inferred_complete_timeline |
| `Action_None` | 263 | 267 | 5 | inferred_complete_timeline |
| `Action_None` | 269 | 272 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 10–250
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 162 | 153 | inferred_complete_timeline |
| `Action_None` | 163 | 250 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 10–15 | 4 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 10–17 | 8 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 36–217 | 177 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 37–62 | 25 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 83–164 | 17 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 176–276 | 80 | 5 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 185–259 | 45 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 186–224 | 21 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 200–256 | 57 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 209–211 | 3 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 217–250 | 34 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 218–278 | 24 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 234–285 | 37 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 235–297 | 63 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 240–275 | 36 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 246–303 | 58 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 282–292 | 11 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 297–350 | 20 | 6 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 323–419 | 96 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 324–331 | 8 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 336–339 | 4 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 340–341 | 2 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 359–383 | 10 | 3 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 360–419 | 59 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 372–419 | 48 | 1 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 377–382 | 4 | 2 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 380–419 | 38 | 2 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 382–387 | 6 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 386–409 | 6 | 2 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 401–414 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (5 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_Handoff` on target `12` (QB)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 30 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 30 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 60 |
| Missing visible bounding boxes during action | 97 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 92 frames exceeds threshold 90 frames [start=166, end=257].
- ⚠️ Segment 'Action_Handoff' for track '12' has invalid range: start=181, end=171. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RT) duration 98 frames exceeds threshold 90 frames [start=166, end=263].
- ⚠️ Action 'Action_None' range [163-247] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-250] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-395] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-255] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-178] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-190] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-272] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-56] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-219] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-41] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [200-210] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [213-217] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [219-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [256-257] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [168-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [174-234] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-175] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [224-239] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [242-243] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-13] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-25] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [169-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-208] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [215-216] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [219-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [247-249] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [251-263] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-17] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-217] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-62] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-76] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [169-177] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [183-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [192-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [212-213] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-229] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-244] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-263] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-247] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-234] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-278] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-246] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-285] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-297] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-275] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-303] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-292] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-328] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-341] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-385] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-331] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-339] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-341] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-379] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-404] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-410] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-387] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-414] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>