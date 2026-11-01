# Play-Annotation-Generator Annotation Review — InsideZoneRead_281

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_281`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 117
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `19` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Keep` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `22` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 15 | START | 15 | 27 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `10` | `9` | 17 | START | 17 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `17` | `16` | 17 | START | 17 | 97 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `17` | 17 | START | 17 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `19` | 17 | START | 17 | 40 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `21` | `20` | 17 | START | 28 | 97 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 27 | END | 15 | 27 |
| ✅ EXACT | `Action_ReadDefender` | QB | `7` | `6` | 36 | START | 36 | 46 |
| ✅ EXACT | `Action_Keep` | QB | `7` | `6` | 47 | START | 47 | 65 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `18` | `17` | 56 | START | 56 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `7` | `6` | 66 | START | 66 | 155 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 97 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_SnapReceive` | 15 | 27 | 13 | inferred_complete_timeline |
| `Action_None` | 28 | 35 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 36 | 46 | 11 | inferred_complete_timeline |
| `Action_Keep` | 47 | 65 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 66 | 155 | 90 | inferred_complete_timeline |
| `Action_BallCarry` | 161 | 163 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 168 | 173 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 176 | 215 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 52 | 38 | inferred_complete_timeline |
| `Action_None` | 55 | 98 | 44 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 219 | 205 | inferred_complete_timeline |
| `Action_None` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 90 | 74 | inferred_complete_timeline |
| `Action_None` | 98 | 239 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 40 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 46 | 60 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 97 | 7 | inferred_complete_timeline |
| `Action_None` | 98 | 239 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_BallSnap` | 15 | 27 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 97 | 70 | inferred_complete_timeline |
| `Action_None` | 98 | 114 | 17 | inferred_complete_timeline |
| `Action_None` | 116 | 123 | 8 | inferred_complete_timeline |
| `Action_None` | 127 | 164 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 55 | 39 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 56 | 97 | 42 | inferred_complete_timeline |
| `Action_None` | 98 | 239 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 17 | 97 | 81 | inferred_complete_timeline |
| `Action_None` | 98 | 113 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 164 | 150 | inferred_complete_timeline |
| `Action_None` | 167 | 199 | 33 | inferred_complete_timeline |
| `Action_None` | 202 | 209 | 8 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 83 | 69 | inferred_complete_timeline |
| `Action_None` | 93 | 239 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 46 | 32 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_None` | 57 | 155 | 99 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 239 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 112 | 98 | inferred_complete_timeline |
| `Action_None` | 114 | 239 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 223 | 209 | inferred_complete_timeline |
| `Action_None` | 225 | 235 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 239 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 188 | 174 | inferred_complete_timeline |
| `Action_None` | 190 | 206 | 17 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 222 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 238 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 98 | 84 | inferred_complete_timeline |
| `Action_None` | 107 | 239 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 235 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 82 | 68 | inferred_complete_timeline |
| `Action_None` | 91 | 215 | 125 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 63–219 | 80 | 15 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 94–215 | 112 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 102–105 | 4 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 104–105 | 2 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 140–239 | 56 | 10 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 142–239 | 98 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 187–239 | 53 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 226–232 | 7 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 231–233 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `21` (C): Annotated start 17 != Inferred start 28
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [15–27], lower_priority='Action_ZoneBlock' annotated_start=17, effective_Action_ZoneBlock_start=28.
- ⚠️ Action 'Action_None' range [15-223] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-235] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-52] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-164] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-199] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-112] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [66-155] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [161-163] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [168-173] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [176-215] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-83] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-239] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-188] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-215] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-219] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-238] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-98] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-239] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [17-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [46-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-114] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-123] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-67] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-98] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-114] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-143] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-166] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-219] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-188] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-215] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-164] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-181] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-199] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '31' has 1 frames without a visible bounding box.
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

</details>