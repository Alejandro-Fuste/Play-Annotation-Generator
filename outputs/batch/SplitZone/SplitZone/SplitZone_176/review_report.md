# Play-Annotation-Generator Annotation Review — SplitZone_176

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_176`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `2` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 3 | START | 4 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 3 | START | 4 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 3 | START | 4 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 3 | START | 4 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 3 | START | 4 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 3 | START | 4 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 3 | START | 4 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 3 | START | 4 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 3 | START | 4 | 128 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 129 | START | 129 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 132 | START | 139 | 145 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `3` | 132 | START | 132 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `5` | 132 | START | 132 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `6` | 132 | START | 132 | 183 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 132 | START | 132 | 220 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 138 | END | 129 | 138 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `11` | `11` | 138 | START | 138 | 170 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 157 | START | 157 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `2` | `2` | 163 | START | 163 | 170 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 220 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 4–226
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_SnapReceive` | 129 | 138 | 10 | inferred_complete_timeline |
| `Action_None` | 139 | 156 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 157 | 162 | 6 | inferred_complete_timeline |
| `Action_None` | 163 | 202 | 40 | inferred_complete_timeline |
| `Action_None` | 205 | 226 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 162 | 159 | inferred_complete_timeline |
| `Action_BallCarry` | 163 | 170 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 177 | 329 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 4–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_None` | 129 | 139 | 11 | inferred_complete_timeline |
| `Action_None` | 147 | 177 | 31 | inferred_complete_timeline |
| `Action_None` | 180 | 251 | 72 | inferred_complete_timeline |
| `Action_None` | 254 | 261 | 8 | inferred_complete_timeline |
| `Action_None` | 263 | 290 | 28 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |
| `Action_None` | 301 | 329 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 4–273
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 137 | 134 | inferred_complete_timeline |
| `Action_SplitBlock` | 138 | 170 | 33 | inferred_complete_timeline |
| `Action_SplitBlock` | 172 | 189 | 18 | inferred_complete_timeline |
| `Action_SplitBlock` | 195 | 220 | 26 | inferred_complete_timeline |
| `Action_None` | 221 | 245 | 25 | inferred_complete_timeline |
| `Action_None` | 249 | 273 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 4–261
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 131 | 128 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 220 | 89 | inferred_complete_timeline |
| `Action_None` | 221 | 261 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 4–264
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 131 | 128 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 173 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 204 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 212 | 220 | 9 | inferred_complete_timeline |
| `Action_None` | 221 | 264 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 4–315
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_BallSnap` | 129 | 138 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 145 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 165 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 220 | 53 | inferred_complete_timeline |
| `Action_None` | 221 | 310 | 90 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–200
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 131 | 128 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 200 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 4–325
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 131 | 128 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 183 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 185 | 220 | 36 | inferred_complete_timeline |
| `Action_None` | 221 | 257 | 37 | inferred_complete_timeline |
| `Action_None` | 259 | 325 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 4–138
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_None` | 129 | 138 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 4–171
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_None` | 129 | 136 | 8 | inferred_complete_timeline |
| `Action_None` | 149 | 171 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 15–67
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 22 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 67 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 4–49
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 49 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 4–254
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_None` | 129 | 199 | 71 | inferred_complete_timeline |
| `Action_None` | 204 | 254 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–154
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_None` | 129 | 154 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 31–316
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 31 | 128 | 98 | inferred_complete_timeline |
| `Action_None` | 129 | 155 | 27 | inferred_complete_timeline |
| `Action_None` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_None` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_None` | 202 | 316 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 4–291
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 128 | 125 | inferred_complete_timeline |
| `Action_None` | 129 | 206 | 78 | inferred_complete_timeline |
| `Action_None` | 226 | 291 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 102–171
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 102 | 128 | 27 | inferred_complete_timeline |
| `Action_None` | 129 | 171 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 4–36 | 29 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 4–17 | 14 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 137–300 | 143 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 161–184 | 24 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 190–258 | 44 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 201–329 | 101 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 202–329 | 126 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 219–329 | 104 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 228–297 | 70 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 268–310 | 43 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 310–329 | 20 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [129–138], lower_priority='Action_ZoneBlock' annotated_start=132, effective_Action_ZoneBlock_start=139.
- ⚠️ Action 'Action_None' range [129-206] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-291] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-199] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-254] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [163-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-200] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-139] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-177] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-251] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-261] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-290] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [176-204] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-264] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-183] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-257] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-325] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-261] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-226] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-49] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [138-170] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [172-189] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-273] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-28] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-36] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-138] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [148-165] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-310] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-136] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-22] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-155] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-316] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-171] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-159] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-248] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-300] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-203] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-258] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-217] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-241] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-220] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-264] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-255] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-290] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-297] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-310] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>