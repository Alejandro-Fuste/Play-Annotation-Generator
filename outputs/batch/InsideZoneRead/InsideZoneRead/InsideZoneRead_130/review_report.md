# Play-Annotation-Generator Annotation Review — InsideZoneRead_130

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_130`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 8
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT | defense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_BlockSecondLevel` | DT | defense | `12` | `11` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 25 | START | 25 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 25 | START | 25 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 25 | START | 25 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 25 | START | 25 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 25 | START | 25 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 25 | START | 25 | 39 |
| ✅ EXACT | `Action_BallSnap` | DT | `12` | `11` | 37 | START | 37 | 48 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `0` | 40 | START | 40 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `6` | `5` | 40 | START | 40 | 100 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `6` | 40 | START | 40 | 100 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 40 | START | 40 | 100 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 48 | END | 37 | 48 |
| ✅ EXACT | `Action_BlockSecondLevel` | DT | `12` | `11` | 53 | START | 53 | 100 |
| ✅ EXACT | `Action_ReadDefender` | QB | `3` | `2` | 53 | START | 53 | 63 |
| ✅ EXACT | `Action_Handoff` | QB | `3` | `2` | 64 | START | 64 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 73 | START | 73 | 194 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 100 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 25–100
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 36 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 37 | 48 | 12 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 53 | 63 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 64 | 72 | 9 | inferred_complete_timeline |
| `Action_None` | 73 | 100 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 25–197
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 71 | 47 | inferred_complete_timeline |
| `Action_BallCarry` | 73 | 194 | 122 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 197 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 25–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 39 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 100 | 61 | inferred_complete_timeline |
| `Action_None` | 101 | 210 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 25–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 39 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 100 | 61 | inferred_complete_timeline |
| `Action_None` | 101 | 210 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 25–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 39 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 100 | 61 | inferred_complete_timeline |
| `Action_None` | 101 | 103 | 3 | inferred_complete_timeline |
| `Action_None` | 106 | 210 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 25–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 39 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 100 | 61 | inferred_complete_timeline |
| `Action_None` | 101 | 210 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 25–210
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 36 | 12 | inferred_complete_timeline |
| `Action_None` | 37 | 65 | 29 | inferred_complete_timeline |
| `Action_None` | 90 | 210 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 26–210
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 36 | 11 | inferred_complete_timeline |
| `Action_None` | 37 | 64 | 28 | inferred_complete_timeline |
| `Action_None` | 67 | 91 | 25 | inferred_complete_timeline |
| `Action_None` | 99 | 210 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 25–133
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 36 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 48 | 12 | inferred_complete_timeline |
| `Action_None` | 49 | 52 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 53 | 100 | 48 | inferred_complete_timeline |
| `Action_None` | 101 | 110 | 10 | inferred_complete_timeline |
| `Action_None` | 113 | 133 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 25–68
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 36 | 12 | inferred_complete_timeline |
| `Action_None` | 37 | 68 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 25–133
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 36 | 12 | inferred_complete_timeline |
| `Action_None` | 37 | 80 | 44 | inferred_complete_timeline |
| `Action_None` | 82 | 85 | 4 | inferred_complete_timeline |
| `Action_None` | 87 | 133 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 25–55
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 36 | 12 | inferred_complete_timeline |
| `Action_None` | 37 | 55 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 25–210
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 36 | 12 | inferred_complete_timeline |
| `Action_None` | 37 | 202 | 166 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 44–142 | 86 | 4 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 46–210 | 162 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 59–136 | 78 | 1 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 72–137 | 50 | 5 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 72–82 | 7 | 2 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 79–101 | 23 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 82–83 | 2 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 98–138 | 32 | 3 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 100–210 | 111 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 118–210 | 93 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 129–132 | 4 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 131–210 | 77 | 2 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 148–183 | 36 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 158–210 | 53 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 159–210 | 35 | 2 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 166–210 | 45 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 170–210 | 41 | 1 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 171–210 | 40 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 180–210 | 31 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 181–210 | 21 | 3 | Undefined position; Undefined team |
| `33` | `50` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 208–210 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 262: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_ZoneBlock' range [40-100] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-65] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-100] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [73-194] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-197] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-55] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-100] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-202] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-133] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-210] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-51] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-120] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-136] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-106] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-76] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-115] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-192] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>