# Play-Annotation-Generator Annotation Review — InsideZoneRead_340

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_340`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 121
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_Keep` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 18 | START | 18 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `9` | 21 | START | 21 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `10` | 21 | START | 28 | 28 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `12` | 21 | START | 21 | 47 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 21 | START | 21 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `7` | 21 | START | 21 | 37 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 27 | END | 18 | 27 |
| ✅ EXACT | `Action_ReadDefender` | QB | `14` | `13` | 30 | START | 30 | 36 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `4` | `3` | 35 | START | 35 | 113 |
| ✅ EXACT | `Action_Keep` | QB | `14` | `13` | 37 | START | 37 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `14` | `13` | 65 | START | 68 | 120 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 113 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–161
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 27 | 10 | inferred_complete_timeline |
| `Action_None` | 28 | 29 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 30 | 36 | 7 | inferred_complete_timeline |
| `Action_Keep` | 37 | 62 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 68 | 120 | 53 | inferred_complete_timeline |
| `Action_BallCarry` | 159 | 161 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 18 | 1 | inferred_complete_timeline |
| `Action_None` | 31 | 75 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 34 | 14 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 35 | 113 | 79 | inferred_complete_timeline |
| `Action_None` | 114 | 147 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 113 | 93 | inferred_complete_timeline |
| `Action_None` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_None` | 144 | 180 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_BallSnap` | 18 | 27 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 28 | 28 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 37 | 67 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 37 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 40 | 99 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 113 | 4 | inferred_complete_timeline |
| `Action_None` | 114 | 142 | 29 | inferred_complete_timeline |
| `Action_None` | 146 | 180 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 47 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 47 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 95 | 78 | inferred_complete_timeline |
| `Action_None` | 98 | 152 | 55 | inferred_complete_timeline |
| `Action_None` | 156 | 180 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_None` | 65 | 151 | 87 | inferred_complete_timeline |
| `Action_None` | 155 | 161 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 76 | 59 | inferred_complete_timeline |
| `Action_None` | 81 | 97 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 92 | 75 | inferred_complete_timeline |
| `Action_None` | 94 | 113 | 20 | inferred_complete_timeline |
| `Action_None` | 118 | 143 | 26 | inferred_complete_timeline |
| `Action_None` | 154 | 180 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 38 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 85 | 68 | inferred_complete_timeline |
| `Action_None` | 171 | 180 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–86 | 87 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 25–180 | 123 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 30–63 | 33 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 55–180 | 97 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 57–180 | 122 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 66–128 | 57 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 69–180 | 112 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 76–180 | 93 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 89–180 | 88 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 90–180 | 91 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 100–139 | 40 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 111–180 | 70 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 122–180 | 59 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 123–180 | 54 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 123–180 | 58 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 126–180 | 53 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 139–155 | 12 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 149–159 | 10 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 149–151 | 3 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 150–180 | 31 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 176–180 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RG) duration 93 frames exceeds threshold 90 frames [start=21, end=113].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (LG) duration 93 frames exceeds threshold 90 frames [start=21, end=113].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [18–27], lower_priority='Action_ZoneBlock' annotated_start=21, effective_Action_ZoneBlock_start=28.
- ⚠️ Action 'Action_None' range [18-38] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-85] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-47] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-34] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-152] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-76] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-62] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-151] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-37] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [40-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-142] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-180] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-86] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [21-113] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '10' starts at frame 28, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [28-28] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [37-67] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 18, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [18-18] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '12' starts at frame 21, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [21-47] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [37-62] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [68-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-108] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-63] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-85] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-71] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-116] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-180] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-139] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-180] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-167] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-167] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-146] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-151] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-180] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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