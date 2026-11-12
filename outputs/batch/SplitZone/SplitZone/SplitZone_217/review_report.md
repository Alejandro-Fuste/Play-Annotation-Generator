# Play-Annotation-Generator Annotation Review — SplitZone_217

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_217`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 2
- **Action Segments:** 108
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 87
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | DE2 | defense | `7` | `7` |
| ⚠️ START CHANGED | `Action_Handoff` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_BallCarry` | LG | offense | `21` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 19 | START | 20 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 19 | START | 20 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 19 | START | 20 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 19 | START | 20 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 19 | START | 20 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 19 | START | 20 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 19 | START | 20 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 19 | START | 20 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 19 | START | 20 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 19 | START | 20 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 19 | START | 20 | 73 |
| ✅ EXACT | `Action_BallSnap` | RT | `17` | `17` | 74 | START | 74 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `17` | 77 | START | 77 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `18` | 77 | START | 77 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `19` | 77 | START | 77 | 131 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `20` | `20` | 77 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `21` | `21` | 77 | START | 77 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | DE2 | `7` | `7` | 84 | START | 84 | 139 |
| ⚠️ START CHANGED | `Action_Handoff` | RG | `20` | `20` | 97 | START | 99 | 102 |
| ✅ EXACT | `Action_SnapReceive` | RG | `20` | `20` | 98 | END | 74 | 98 |
| ✅ EXACT | `Action_BallCarry` | LG | `21` | `21` | 103 | START | 103 | 106 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 185 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 20–153
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 147 | 74 | inferred_complete_timeline |
| `Action_None` | 149 | 153 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 329 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 329 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 20–266
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 177 | 104 | inferred_complete_timeline |
| `Action_None` | 180 | 266 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 20–304
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 138 | 65 | inferred_complete_timeline |
| `Action_None` | 142 | 291 | 150 | inferred_complete_timeline |
| `Action_None` | 295 | 304 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 329 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 76 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 185 | 109 | inferred_complete_timeline |
| `Action_None` | 186 | 329 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 20–106
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 40 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 76 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 92 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 98 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 102 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 106 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 20–329
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 76 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 131 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 147 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 150 | 164 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 185 | 16 | inferred_complete_timeline |
| `Action_None` | 186 | 190 | 5 | inferred_complete_timeline |
| `Action_None` | 195 | 290 | 96 | inferred_complete_timeline |
| `Action_None` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 20–289
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 98 | 25 | inferred_complete_timeline |
| `Action_Handoff` | 99 | 102 | 4 | inferred_complete_timeline |
| `Action_None` | 103 | 289 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 20–125
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 94 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 115 | 119 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 125 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 20–321
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 123 | 50 | inferred_complete_timeline |
| `Action_None` | 125 | 291 | 167 | inferred_complete_timeline |
| `Action_None` | 304 | 321 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 83 | 64 | inferred_complete_timeline |
| `Action_SplitBlock` | 84 | 139 | 56 | inferred_complete_timeline |
| `Action_SplitBlock` | 141 | 185 | 45 | inferred_complete_timeline |
| `Action_None` | 186 | 238 | 53 | inferred_complete_timeline |
| `Action_None` | 243 | 312 | 70 | inferred_complete_timeline |
| `Action_None` | 314 | 329 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 329 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 329 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 20–125
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 125 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 20–316
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 316 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 20–292
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 154 | 81 | inferred_complete_timeline |
| `Action_None` | 162 | 292 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 313 | 240 | inferred_complete_timeline |
| `Action_None` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_None` | 324 | 329 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 20–271
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 261 | 188 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 20–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 329 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 20–123
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 73 | 54 | inferred_complete_timeline |
| `Action_None` | 74 | 123 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 115–329 | 211 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 117–329 | 213 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 120–121 | 2 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 130–329 | 187 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 138–329 | 192 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 156–177 | 22 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 158–159 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 179–329 | 151 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 224–233 | 7 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 227–233 | 6 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 232–291 | 52 | 3 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 245–251 | 7 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 249–262 | 8 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 282–329 | 48 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 292–328 | 17 | 3 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 301–302 | 2 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 303–329 | 27 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 306–329 | 14 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `33` | `41` | 238 | 251 | 12 | 85.7% | 245–246 |
| `41` | `55` | 317 | 329 | 7 | 53.8% | 321–326 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (4 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `20` (RG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `7` (2 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `20` (RG): Annotated start 97 != Inferred start 99

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 109 frames exceeds threshold 90 frames [start=77, end=185].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (C) duration 109 frames exceeds threshold 90 frames [start=77, end=185].
- ⚠️ Action 'Action_None' range [74-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-266] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-138] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-291] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-304] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [84-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-312] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-316] for track '8' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-291] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-321] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-261] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-125] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-313] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-154] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-292] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-94] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [105-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [115-119] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [150-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-290] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-289] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-76] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-98] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-106] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-251] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-257] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-138] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-329] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-177] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-270] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-282] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-329] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-294] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-313] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-310] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '40' has 1 frames without a visible bounding box.
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