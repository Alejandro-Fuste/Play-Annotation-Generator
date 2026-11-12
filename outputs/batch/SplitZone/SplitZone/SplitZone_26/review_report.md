# Play-Annotation-Generator Annotation Review — SplitZone_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_26`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 35
- **Ball Tracks:** 2
- **Action Segments:** 88
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `0` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 109 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 107 | START | 107 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `1` | `1` | 110 | START | 110 | 166 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `10` | `10` | 110 | START | 110 | 220 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `14` | `14` | 110 | START | 120 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `2` | 110 | START | 110 | 193 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 110 | START | 110 | 220 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | HB | `0` | `0` | 113 | START | 113 | 165 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 119 | END | 107 | 119 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 135 | START | 135 | 145 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `11` | 146 | START | 159 | 161 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 220 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–353
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_SnapReceive` | 107 | 119 | 13 | inferred_complete_timeline |
| `Action_None` | 120 | 134 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 135 | 145 | 11 | inferred_complete_timeline |
| `Action_None` | 146 | 190 | 45 | inferred_complete_timeline |
| `Action_None` | 250 | 353 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_BallCarry` | 159 | 161 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 165 | 340 | 176 | inferred_complete_timeline |
| `Action_BallCarry` | 350 | 359 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_SplitBlock` | 113 | 165 | 53 | inferred_complete_timeline |
| `Action_SplitBlock` | 200 | 201 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 220 | 111 | inferred_complete_timeline |
| `Action_None` | 221 | 251 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 193 | 84 | inferred_complete_timeline |
| `Action_ZoneBlock` | 201 | 220 | 20 | inferred_complete_timeline |
| `Action_None` | 221 | 228 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_BallSnap` | 107 | 119 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 197 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 166 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 204 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 220 | 111 | inferred_complete_timeline |
| `Action_None` | 221 | 234 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 6–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 17 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 106 | 86 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 237 | 128 | inferred_complete_timeline |
| `Action_None` | 239 | 359 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 136 | 30 | inferred_complete_timeline |
| `Action_None` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 125 | 19 | inferred_complete_timeline |
| `Action_None` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_None` | 146 | 180 | 35 | inferred_complete_timeline |
| `Action_None` | 182 | 183 | 2 | inferred_complete_timeline |
| `Action_None` | 185 | 218 | 34 | inferred_complete_timeline |
| `Action_None` | 224 | 230 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 119 | 13 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 145 | 16 | inferred_complete_timeline |
| `Action_None` | 167 | 198 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 155 | 49 | inferred_complete_timeline |
| `Action_None` | 159 | 164 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 147 | 41 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_None` | 107 | 214 | 108 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 34–35 | 2 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 150–263 | 111 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 165–174 | 10 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 173–185 | 12 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 191–359 | 158 | 3 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 202–243 | 29 | 3 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 214–226 | 13 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 216–237 | 22 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 218–220 | 3 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 219–241 | 23 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 234–261 | 28 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 245–351 | 107 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 264–337 | 71 | 3 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 275–286 | 12 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 312–359 | 48 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 347–359 | 13 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 349–359 | 7 | 2 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 354–359 | 6 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 355–359 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | 6 | 12 | 2 | 28.6% | 7–11 |
| `23` | `31` | 203 | 205 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `14` (C): Annotated start 110 != Inferred start 120
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RG) duration 95 frames exceeds threshold 90 frames [start=110, end=204].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '2' (LG) duration 111 frames exceeds threshold 90 frames [start=110, end=220].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 111 frames exceeds threshold 90 frames [start=110, end=220].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (LT) duration 111 frames exceeds threshold 90 frames [start=110, end=220].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [107–119], lower_priority='Action_ZoneBlock' annotated_start=110, effective_Action_ZoneBlock_start=120.
- ⚠️ Action 'Action_SplitBlock' range [113-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [200-201] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-166] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [170-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-204] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-193] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-228] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-198] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-147] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-125] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-218] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-251] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-161] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [165-340] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [350-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-190] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-353] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-197] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-106] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-237] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-220] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-263] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-261] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-324] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-212] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-226] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-241] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-261] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-351] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-286] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-308] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-337] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-286] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-354] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
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