# Play-Annotation-Generator Annotation Review — JetSweep_165

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_165`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR3 | offense | `13` | `12` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 77 |
| ✅ EXACT | `Action_JetMotion` | WR3 | `13` | `12` | 31 | START | 31 | 98 |
| ✅ EXACT | `Action_BallSnap` | LG | `14` | `13` | 78 | START | 78 | 78 |
| ✅ EXACT | `Action_LeadBlock` | TE | `4` | `3` | 79 | START | 79 | 104 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `13` | 79 | START | 79 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `18` | 79 | START | 79 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 79 | START | 79 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `21` | `20` | 79 | START | 79 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 79 | START | 79 | 95 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 86 | END | 78 | 86 |
| ✅ EXACT | `Action_Toss` | QB | `10` | `9` | 93 | START | 93 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `13` | `12` | 99 | START | 99 | 217 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 104 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_SnapReceive` | 78 | 86 | 9 | inferred_complete_timeline |
| `Action_None` | 87 | 92 | 6 | inferred_complete_timeline |
| `Action_Toss` | 93 | 98 | 6 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 299 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 299 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 205 | 128 | inferred_complete_timeline |
| `Action_None` | 214 | 299 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_JetMotion` | 31 | 98 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 99 | 217 | 119 | inferred_complete_timeline |
| `Action_BallCarry` | 219 | 220 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_LeadBlock` | 79 | 104 | 26 | inferred_complete_timeline |
| `Action_None` | 105 | 299 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 104 | 26 | inferred_complete_timeline |
| `Action_None` | 105 | 137 | 33 | inferred_complete_timeline |
| `Action_None` | 139 | 204 | 66 | inferred_complete_timeline |
| `Action_None` | 208 | 299 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_BallSnap` | 78 | 78 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 87 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 79 | 1 | inferred_complete_timeline |
| `Action_None` | 115 | 299 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–284
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 95 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 104 | 8 | inferred_complete_timeline |
| `Action_None` | 105 | 111 | 7 | inferred_complete_timeline |
| `Action_None` | 115 | 284 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ZoneBlock` | 79 | 104 | 26 | inferred_complete_timeline |
| `Action_None` | 105 | 131 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 299 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 299 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 137 | 60 | inferred_complete_timeline |
| `Action_None` | 141 | 169 | 29 | inferred_complete_timeline |
| `Action_None` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 99 | 22 | inferred_complete_timeline |
| `Action_None` | 104 | 135 | 32 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 299 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 172 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 154 | 77 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 299 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 282 | 205 | inferred_complete_timeline |
| `Action_None` | 284 | 292 | 9 | inferred_complete_timeline |
| `Action_None` | 294 | 298 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 283 | 206 | inferred_complete_timeline |
| `Action_None` | 286 | 299 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 299 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 274 | 197 | inferred_complete_timeline |
| `Action_None` | 276 | 299 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 299 | 222 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 94–108 | 15 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 107–299 | 192 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 124–129 | 6 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 143–299 | 157 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 171–299 | 123 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 184–245 | 32 | 9 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 187–191 | 4 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 214–215 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 215–291 | 46 | 6 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 233–288 | 54 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 241–287 | 26 | 4 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 257–271 | 13 | 2 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 290–299 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 62 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [78-205] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-282] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-292] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-298] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-172] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-154] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-274] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-99] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-135] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [99-217] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [219-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-283] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-104] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-131] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-204] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '20' starts at frame 79, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [79-79] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [79-95] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-284] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-224] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-129] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-222] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-233] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-252] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-274] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-288] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-258] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-261] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-271] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-296] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '35' has 1 frames without a visible bounding box.
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