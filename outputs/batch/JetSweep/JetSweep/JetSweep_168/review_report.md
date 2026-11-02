# Play-Annotation-Generator Annotation Review — JetSweep_168

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_168`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | TE | offense | `7` | `6` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `18` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 22 |
| ✅ EXACT | `Action_BallSnap` | TE | `7` | `6` | 21 | START | 21 | 22 |
| ✅ EXACT | `Action_LeadBlock` | TE | `7` | `6` | 23 | START | 23 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `16` | `15` | 23 | START | 23 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `16` | 23 | START | 23 | 23 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `5` | 23 | START | 23 | 61 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `8` | `7` | 23 | START | 23 | 49 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `8` | 23 | START | 23 | 61 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 32 | END | 21 | 32 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 44 | START | 44 | 51 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `18` | `17` | 52 | START | 52 | 67 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 61 | BOUNDARY | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `18` | `17` | 68 | START | 68 | 84 |

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
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 32 | 12 | inferred_complete_timeline |
| `Action_None` | 33 | 43 | 11 | inferred_complete_timeline |
| `Action_Toss` | 44 | 51 | 8 | inferred_complete_timeline |
| `Action_None` | 52 | 95 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 98 | 78 | inferred_complete_timeline |
| `Action_None` | 102 | 170 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_BallSnap` | 21 | 22 | 2 | inferred_complete_timeline |
| `Action_LeadBlock` | 23 | 61 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 48 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 54 | 56 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 63 | 68 | 6 | inferred_complete_timeline |
| `Action_None` | 72 | 125 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 49 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_None` | 62 | 142 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 23 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 29 | 57 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 61 | 61 | 1 | inferred_complete_timeline |
| `Action_None` | 62 | 172 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 61 | 39 | inferred_complete_timeline |
| `Action_None` | 62 | 102 | 41 | inferred_complete_timeline |
| `Action_None` | 106 | 110 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 23 | 61 | 39 | inferred_complete_timeline |
| `Action_None` | 62 | 193 | 132 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 163 | 143 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 188 | 168 | inferred_complete_timeline |
| `Action_None` | 190 | 196 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 116 | 96 | inferred_complete_timeline |
| `Action_None` | 120 | 180 | 61 | inferred_complete_timeline |
| `Action_None` | 185 | 210 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 76 | 56 | inferred_complete_timeline |
| `Action_None` | 78 | 210 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 210 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 92 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_None` | 21 | 43 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 20–209 | 187 | 5 | Undefined position; Undefined team |
| `18` | `26` | Position_Unknown | Team_Unknown | 83–84 | 2 | 1 | Undefined position; Undefined team |
| `19` | `29` | Position_Unknown | Team_Unknown | 93–123 | 31 | 1 | Undefined position; Undefined team |
| `20` | `30` | Position_Unknown | Team_Unknown | 93–135 | 16 | 3 | Undefined position; Undefined team |
| `21` | `32` | Position_Unknown | Team_Unknown | 95–100 | 6 | 1 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 97–106 | 8 | 2 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 117–118 | 2 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 117–163 | 43 | 2 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 119–161 | 43 | 1 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 130–180 | 45 | 2 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 159–160 | 2 | 1 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 186–210 | 25 | 1 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 187–210 | 24 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 191–210 | 17 | 2 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 202–210 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_JetMotion` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 57 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [21-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-92] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-43] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-98] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-193] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [23-61] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-49] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-142] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-102] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-163] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-188] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-76] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-116] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-180] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [23-48] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [54-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [60-61] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-125] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '16' starts at frame 23, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [23-23] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [29-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-172] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [68-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [87-198] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [200-209] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-100] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-106] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-163] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-161] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-145] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-197] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '32' has 2 frames without a visible bounding box.
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

</details>