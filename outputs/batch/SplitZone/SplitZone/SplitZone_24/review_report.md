# Play-Annotation-Generator Annotation Review — SplitZone_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_24`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `0` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 10 | START | 10 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 10 | START | 10 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 10 | START | 10 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 10 | START | 10 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 10 | START | 10 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 10 | START | 10 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `4` | `Group` | 10 | START | 10 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 10 | START | 10 | 59 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 60 | START | 60 | 76 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `1` | `1` | 63 | START | 63 | 81 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `11` | `11` | 63 | START | 77 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `12` | 63 | START | 63 | 90 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `14` | 63 | START | 63 | 134 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 63 | START | 63 | 134 |
| ✅ EXACT | `Action_SplitBlock` | HB | `4` | `4` | 66 | START | 66 | 92 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 76 | END | 60 | 76 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 85 | START | 85 | 96 |
| ✅ EXACT | `Action_BallCarry` | RB | `0` | `0` | 97 | START | 97 | 97 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 134 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 10–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 59 | 50 | inferred_complete_timeline |
| `Action_SnapReceive` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_None` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 85 | 96 | 12 | inferred_complete_timeline |
| `Action_None` | 97 | 222 | 126 | inferred_complete_timeline |
| `Action_None` | 225 | 239 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 10–97
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 96 | 87 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 97 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 10–92
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 65 | 56 | inferred_complete_timeline |
| `Action_SplitBlock` | 66 | 92 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 10–178
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 62 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 134 | 72 | inferred_complete_timeline |
| `Action_None` | 135 | 178 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 10–81
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 62 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 81 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 10–131
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 59 | 50 | inferred_complete_timeline |
| `Action_BallSnap` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 131 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 10–192
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 62 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 90 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 134 | 43 | inferred_complete_timeline |
| `Action_None` | 135 | 192 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 10–190
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 62 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 63 | 134 | 72 | inferred_complete_timeline |
| `Action_None` | 135 | 174 | 40 | inferred_complete_timeline |
| `Action_None` | 179 | 190 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 10–168
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 59 | 50 | inferred_complete_timeline |
| `Action_None` | 60 | 89 | 30 | inferred_complete_timeline |
| `Action_None` | 102 | 168 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 10–239
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 59 | 50 | inferred_complete_timeline |
| `Action_None` | 60 | 103 | 44 | inferred_complete_timeline |
| `Action_None` | 142 | 229 | 88 | inferred_complete_timeline |
| `Action_None` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 10–168
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 59 | 50 | inferred_complete_timeline |
| `Action_None` | 60 | 72 | 13 | inferred_complete_timeline |
| `Action_None` | 84 | 168 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 10–132
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 25 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 59 | 19 | inferred_complete_timeline |
| `Action_None` | 60 | 64 | 5 | inferred_complete_timeline |
| `Action_None` | 97 | 102 | 6 | inferred_complete_timeline |
| `Action_None` | 113 | 132 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 10–239
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 59 | 50 | inferred_complete_timeline |
| `Action_None` | 60 | 94 | 35 | inferred_complete_timeline |
| `Action_None` | 152 | 170 | 19 | inferred_complete_timeline |
| `Action_None` | 172 | 219 | 48 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 10–154
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 59 | 50 | inferred_complete_timeline |
| `Action_None` | 60 | 90 | 31 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 102 | 109 | 8 | inferred_complete_timeline |
| `Action_None` | 111 | 154 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 10–28
- **Visible Samples:** 19

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 28 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 10–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 59 | 50 | inferred_complete_timeline |
| `Action_None` | 60 | 118 | 59 | inferred_complete_timeline |
| `Action_None` | 122 | 188 | 67 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 239 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 23–24 | 2 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 45–142 | 84 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 99–219 | 121 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 102–142 | 15 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 113–169 | 47 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 125–170 | 46 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 130–239 | 110 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 142–239 | 98 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 162–239 | 78 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 196–202 | 7 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 205–239 | 30 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 206–239 | 34 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 208–239 | 22 | 4 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 211–239 | 29 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 234–235 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `11` (C): Annotated start 63 != Inferred start 77
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [60–76], lower_priority='Action_ZoneBlock' annotated_start=63, effective_Action_ZoneBlock_start=77.
- ⚠️ Action 'Action_BallCarry' for track '0' starts at frame 97, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [97-97] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-81] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-134] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-190] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-103] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-229] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [66-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-94] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-170] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-72] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-168] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-28] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-222] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-109] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-154] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-89] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-168] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-131] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [63-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-188] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-178] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-132] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-111] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-219] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-108] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-202] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-212] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-231] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '31' has 1 frames without a visible bounding box.
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

</details>