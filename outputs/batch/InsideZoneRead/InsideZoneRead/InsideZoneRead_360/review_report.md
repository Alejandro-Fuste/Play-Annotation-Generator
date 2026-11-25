# Play-Annotation-Generator Annotation Review — InsideZoneRead_360

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_360`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 84
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
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | DE1 | defense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | DE1 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | DE1 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | defense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | RG | `12` | `11` | 26 | START | 26 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 29 | START | 29 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `11` | 29 | START | 29 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `4` | 29 | START | 29 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `5` | 29 | START | 29 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `7` | 29 | START | 29 | 61 |
| ✅ EXACT | `Action_SnapReceive` | DE1 | `9` | `8` | 39 | END | 26 | 39 |
| ✅ EXACT | `Action_ReadDefender` | DE1 | `9` | `8` | 47 | START | 47 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | DE1 | `9` | `8` | 54 | START | 54 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | `9` | `8` | 68 | START | 68 | 78 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 86 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 28 | 3 | inferred_complete_timeline |
| `Action_None` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_None` | 42 | 59 | 18 | inferred_complete_timeline |
| `Action_None` | 61 | 94 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 32 | 7 | inferred_complete_timeline |
| `Action_None` | 34 | 78 | 45 | inferred_complete_timeline |
| `Action_None` | 84 | 140 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–45
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 40 | 15 | inferred_complete_timeline |
| `Action_None` | 43 | 45 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 86 | 58 | inferred_complete_timeline |
| `Action_None` | 87 | 94 | 8 | inferred_complete_timeline |
| `Action_None` | 99 | 123 | 25 | inferred_complete_timeline |
| `Action_None` | 130 | 239 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 61 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 82 | 20 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 106 | 209 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 86 | 58 | inferred_complete_timeline |
| `Action_None` | 87 | 198 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_BallSnap` | 26 | 28 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 47 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 49 | 86 | 38 | inferred_complete_timeline |
| `Action_None` | 90 | 123 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 43 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 45 | 60 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 84 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 39 | 14 | inferred_complete_timeline |
| `Action_None` | 40 | 46 | 7 | inferred_complete_timeline |
| `Action_ReadDefender` | 47 | 53 | 7 | inferred_complete_timeline |
| `Action_Keep` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_Keep` | 62 | 67 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 68 | 78 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 82 | 239 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 66 | 41 | inferred_complete_timeline |
| `Action_None` | 69 | 146 | 78 | inferred_complete_timeline |
| `Action_None` | 150 | 239 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 238 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 116 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 81 | 56 | inferred_complete_timeline |
| `Action_None` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_None` | 92 | 239 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 183 | 158 | inferred_complete_timeline |
| `Action_None` | 185 | 239 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 106 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 192 | 167 | inferred_complete_timeline |
| `Action_None` | 195 | 234 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 46–47 | 2 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 52–55 | 4 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 70–78 | 9 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 93–239 | 128 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 100–232 | 124 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 150–239 | 90 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 162–239 | 75 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 170–235 | 66 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 176–239 | 64 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 178–196 | 16 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 178–239 | 43 | 2 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 223–226 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Keep` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 58 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [26-106] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-81] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-90] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-183] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-192] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-234] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-94] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-239] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-43] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [45-60] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-69] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-84] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-116] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-61] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-82] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-209] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [54-57] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [68-78] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-66] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-86] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-198] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [49-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-238] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-28] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-94] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-140] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-160] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-214] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-223] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-201] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-239] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-235] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-205] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '27' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_360'; source metadata written as null.

</details>