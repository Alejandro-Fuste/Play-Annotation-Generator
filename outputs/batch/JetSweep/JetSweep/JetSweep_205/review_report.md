# Play-Annotation-Generator Annotation Review — JetSweep_205

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_205`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 54
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `3` | `2` |
| ✅ EXACT | `Action_LeadBlock` | TE2 | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `11` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 128 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 137 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `3` | `2` | 91 | START | 91 | 153 |
| ✅ EXACT | `Action_LeadBlock` | TE2 | `11` | `10` | 129 | START | 129 | 240 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `13` | `12` | 129 | START | 129 | 240 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `18` | `17` | 129 | START | 129 | 222 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 129 | START | 129 | 240 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 129 | START | 129 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 129 | START | 129 | 140 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 138 | START | 138 | 140 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 140 | END | 138 | 140 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 148 | START | 148 | 153 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `3` | `2` | 154 | START | 154 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 240 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_SnapReceive` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 147 | 7 | inferred_complete_timeline |
| `Action_Toss` | 148 | 153 | 6 | inferred_complete_timeline |
| `Action_None` | 154 | 247 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 299 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 197 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_JetMotion` | 91 | 153 | 63 | inferred_complete_timeline |
| `Action_BallCarry` | 154 | 299 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 294 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_LeadBlock` | 129 | 240 | 112 | inferred_complete_timeline |
| `Action_None` | 241 | 299 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 240 | 112 | inferred_complete_timeline |
| `Action_None` | 241 | 299 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 240 | 112 | inferred_complete_timeline |
| `Action_None` | 241 | 299 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_None` | 129 | 137 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 299 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 140 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 201 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 205 | 215 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |
| `Action_ZoneBlock` | 129 | 222 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 148 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 299 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 299 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 299 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 269 | 132 | inferred_complete_timeline |
| `Action_None` | 271 | 299 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 177 | 40 | inferred_complete_timeline |
| `Action_None` | 180 | 228 | 49 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 299 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 194 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 199 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 294 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 273 | 136 | inferred_complete_timeline |
| `Action_None` | 280 | 288 | 9 | inferred_complete_timeline |
| `Action_None` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 233 | 96 | inferred_complete_timeline |
| `Action_None` | 238 | 240 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–167 | 147 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 139–144 | 6 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 159–299 | 141 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 238–299 | 44 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 270–299 | 30 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 272–299 | 28 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 285–299 | 13 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 295–296 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 32 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 112 frames exceeds threshold 90 frames [start=129, end=240].
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '10' (TE2) duration 112 frames exceeds threshold 90 frames [start=129, end=240].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (LG) duration 112 frames exceeds threshold 90 frames [start=129, end=240].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (RT) duration 94 frames exceeds threshold 90 frames [start=129, end=222].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [138–140], lower_priority='Action_ZoneBlock' annotated_start=129, effective_Action_ZoneBlock_start=141.
- ⚠️ Action 'Action_None' range [138-197] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-240] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-233] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-177] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-228] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-273] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-288] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-247] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-294] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-222] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-294] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [129-140] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-201] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [205-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-134] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-167] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-248] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '29' has 1 frames without a visible bounding box.
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