# Play-Annotation-Generator Annotation Review — SplitZone_156

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_156`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 9
- **Group Expanded Events:** 9
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | TE2 | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `15` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `1` | `1` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | TE2 | offense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 17 | START | 18 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 17 | START | 18 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 17 | START | 18 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `14` | `Group` | 17 | START | 18 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 17 | START | 18 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 17 | START | 18 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 17 | START | 18 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 17 | START | 18 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 17 | START | 18 | 64 |
| ✅ EXACT | `Action_BallSnap` | TE2 | `14` | `14` | 63 | START | 63 | 69 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `11` | 65 | START | 65 | 131 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `12` | 65 | START | 65 | 132 |
| ✅ EXACT | `Action_ZoneBlock` | C | `16` | `16` | 65 | START | 65 | 132 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `4` | 65 | START | 65 | 132 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `7` | `7` | 65 | START | 65 | 70 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 69 | END | 63 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `15` | `15` | 70 | START | 70 | 76 |
| ✅ EXACT | `Action_Handoff` | QB | `17` | `17` | 86 | START | 86 | 96 |
| ✅ EXACT | `Action_BallCarry` | RB | `1` | `1` | 97 | START | 97 | 117 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | TE2 | `14` | `14` | 97 | START | 109 | 110 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 132 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 18–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_None` | 70 | 85 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 86 | 96 | 11 | inferred_complete_timeline |
| `Action_None` | 97 | 210 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 18–117
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 96 | 79 | inferred_complete_timeline |
| `Action_BallCarry` | 97 | 117 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 18–210
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 69 | 52 | inferred_complete_timeline |
| `Action_SplitBlock` | 70 | 76 | 7 | inferred_complete_timeline |
| `Action_SplitBlock` | 90 | 122 | 33 | inferred_complete_timeline |
| `Action_SplitBlock` | 132 | 132 | 1 | inferred_complete_timeline |
| `Action_None` | 133 | 210 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 18–110
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_BallSnap` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_None` | 70 | 84 | 15 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 109 | 110 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 18–70
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 64 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 70 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 18–131
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 64 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 131 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 18–192
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 64 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 132 | 68 | inferred_complete_timeline |
| `Action_None` | 133 | 140 | 8 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 155 | 192 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 18–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 64 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 132 | 68 | inferred_complete_timeline |
| `Action_None` | 133 | 210 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 18–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 64 | 47 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 132 | 68 | inferred_complete_timeline |
| `Action_None` | 133 | 210 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 18–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_None` | 63 | 96 | 34 | inferred_complete_timeline |
| `Action_None` | 100 | 210 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 18–210
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_None` | 63 | 176 | 114 | inferred_complete_timeline |
| `Action_None` | 188 | 210 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 18–210
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_None` | 63 | 114 | 52 | inferred_complete_timeline |
| `Action_None` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_None` | 162 | 210 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 18–210
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_None` | 63 | 130 | 68 | inferred_complete_timeline |
| `Action_None` | 135 | 144 | 10 | inferred_complete_timeline |
| `Action_None` | 149 | 210 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 18–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_None` | 63 | 110 | 48 | inferred_complete_timeline |
| `Action_None` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_None` | 117 | 125 | 9 | inferred_complete_timeline |
| `Action_None` | 129 | 210 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 18–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_None` | 63 | 210 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 18–210
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_None` | 63 | 210 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 18–103
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_None` | 63 | 103 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 18–210
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 31 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 62 | 30 | inferred_complete_timeline |
| `Action_None` | 63 | 140 | 78 | inferred_complete_timeline |
| `Action_None` | 142 | 186 | 45 | inferred_complete_timeline |
| `Action_None` | 190 | 210 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 62–210 | 149 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 68–210 | 143 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 70–89 | 4 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 72–187 | 83 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 79–107 | 23 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 97–190 | 66 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 122–210 | 88 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 125–182 | 58 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 128–134 | 7 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 156–210 | 54 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 156–157 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 164–210 | 47 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 166–210 | 45 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 179–210 | 32 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 187–194 | 8 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 191–210 | 20 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 193–210 | 18 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `15` (3 segments found)
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `14` (TE2): Annotated start 97 != Inferred start 109

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 61 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [63-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [97-117] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-130] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-31] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-140] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-176] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-70] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-62] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-103] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-110] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-131] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-96] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [109-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [70-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [90-122] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-140] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-192] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-107] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-190] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-140] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-134] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-194] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '34' has 1 frames without a visible bounding box.
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