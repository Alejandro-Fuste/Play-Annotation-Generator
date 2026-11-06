# Play-Annotation-Generator Annotation Review — OutsideZoneRead_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_67`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | Team_Unknown | `22` | `22` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 196 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 195 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 419 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 195 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | `22` | `22` | 117 | START | 117 | 198 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `17` | `17` | 196 | START | 196 | 233 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `18` | 196 | START | 196 | 233 |
| ✅ EXACT | `Action_ZoneBlock` | C | `19` | `19` | 196 | START | 196 | 233 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `20` | `20` | 196 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RG | `8` | `8` | 196 | START | 196 | 233 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `11` | `11` | 197 | START | 197 | 212 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `11` | 213 | START | 213 | 219 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 197 | 212 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 213 | 219 | 7 | inferred_complete_timeline |
| `Action_None` | 220 | 419 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 233 | 38 | inferred_complete_timeline |
| `Action_None` | 234 | 278 | 45 | inferred_complete_timeline |
| `Action_None` | 280 | 419 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 70 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 233 | 38 | inferred_complete_timeline |
| `Action_None` | 234 | 256 | 23 | inferred_complete_timeline |
| `Action_None` | 267 | 419 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 233 | 38 | inferred_complete_timeline |
| `Action_None` | 234 | 419 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_ZoneBlock` | 196 | 233 | 38 | inferred_complete_timeline |
| `Action_None` | 234 | 419 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 226 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 237 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 391 | 392 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 419 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 262 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 272 | 273 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 419 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 413 | 414 | inferred_complete_timeline |
| `Action_PreSnap` | 419 | 419 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–407
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 407 | 408 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 419 | 420 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 11–269 | 247 | 6 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 40–419 | 372 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 237–419 | 183 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 266–419 | 154 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 267–270 | 4 | 1 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 282–419 | 136 | 2 | Undefined position; Undefined team |
| `27` | `27` | Position_Unknown | Team_Unknown | 284–330 | 41 | 3 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 315–406 | 77 | 5 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 325–326 | 2 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 350–352 | 3 | 1 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 355–356 | 2 | 1 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 357–419 | 54 | 6 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 365–367 | 3 | 1 | Undefined position; Undefined team |
| `34` | `36` | Position_Unknown | Team_Unknown | 366–367 | 2 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 372–419 | 46 | 3 | Undefined position; Undefined team |
| `36` | `40` | Position_Unknown | Team_Unknown | 378–379 | 2 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 396–417 | 10 | 3 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 406–414 | 8 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 413–419 | 3 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `22` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `20` (LG)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '20' has invalid range: start=196, end=70. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-216] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-237] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-419] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-391] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-413] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-272] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-419] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-407] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-278] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [196-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-256] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-419] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-13] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-19] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-251] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-63] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [117-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-419] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-270] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-294] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-318] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-324] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-330] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-343] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-367] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-381] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-393] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-406] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-326] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-352] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-356] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-361] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-365] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-377] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-387] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-367] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-367] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-377] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-416] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-419] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-379] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-397] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-402] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-417] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [406-408] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-414] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-414] for track '39' has 1 frames without a visible bounding box.
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

</details>