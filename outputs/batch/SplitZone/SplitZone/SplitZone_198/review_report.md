# Play-Annotation-Generator Annotation Review — SplitZone_198

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_198`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `3` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `11` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `0` | `Group` | 5 | START | 6 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 5 | START | 6 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 5 | START | 6 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 5 | START | 6 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 5 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 5 | START | 6 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 5 | START | 6 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 5 | START | 6 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 5 | START | 6 | 86 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 84 | START | 84 | 84 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB | `18` | `17` | 85 | END | 94 | 94 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `0` | `0` | 87 | START | 87 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `15` | `15` | 87 | START | 87 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `2` | `2` | 87 | START | 87 | 116 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 87 | START | 87 | 149 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `8` | 87 | START | 87 | 149 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `3` | `3` | 91 | START | 91 | 114 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 100 | START | 100 | 110 |
| ✅ EXACT | `Action_BallCarry` | RB | `11` | `11` | 111 | START | 111 | 158 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 149 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 94–137
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_SnapReceive` | 94 | 94 | 1 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 99 | 99 | 1 | inferred_complete_timeline |
| `Action_Handoff` | 100 | 110 | 11 | inferred_complete_timeline |
| `Action_None` | 111 | 137 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 6–158
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 110 | 105 | inferred_complete_timeline |
| `Action_BallCarry` | 111 | 158 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 6–114
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 90 | 85 | inferred_complete_timeline |
| `Action_SplitBlock` | 91 | 114 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 6–196
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 83 | 78 | inferred_complete_timeline |
| `Action_None` | 84 | 177 | 94 | inferred_complete_timeline |
| `Action_None` | 180 | 183 | 4 | inferred_complete_timeline |
| `Action_None` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 6–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 86 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 149 | 63 | inferred_complete_timeline |
| `Action_None` | 150 | 269 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 6–268
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 86 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 116 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 122 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 125 | 140 | 16 | inferred_complete_timeline |
| `Action_None` | 150 | 263 | 114 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 6–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 79 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 83 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 84 | 84 | 1 | inferred_complete_timeline |
| `Action_None` | 86 | 86 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 111 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 149 | 37 | inferred_complete_timeline |
| `Action_None` | 150 | 269 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 6–103
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 86 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 103 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 6–151
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 86 | 81 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 149 | 63 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 83 | 78 | inferred_complete_timeline |
| `Action_None` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_None` | 101 | 157 | 57 | inferred_complete_timeline |
| `Action_None` | 159 | 269 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 6–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 83 | 78 | inferred_complete_timeline |
| `Action_None` | 84 | 208 | 125 | inferred_complete_timeline |
| `Action_None` | 210 | 269 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 6–118
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 83 | 78 | inferred_complete_timeline |
| `Action_None` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_None` | 99 | 108 | 10 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–134
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 83 | 78 | inferred_complete_timeline |
| `Action_None` | 84 | 96 | 13 | inferred_complete_timeline |
| `Action_None` | 102 | 105 | 4 | inferred_complete_timeline |
| `Action_None` | 110 | 129 | 20 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–105
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 83 | 78 | inferred_complete_timeline |
| `Action_None` | 84 | 105 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 6–265
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 83 | 78 | inferred_complete_timeline |
| `Action_None` | 84 | 115 | 32 | inferred_complete_timeline |
| `Action_None` | 125 | 131 | 7 | inferred_complete_timeline |
| `Action_None` | 133 | 265 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 6–207
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 83 | 78 | inferred_complete_timeline |
| `Action_None` | 84 | 207 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 6–145
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 83 | 78 | inferred_complete_timeline |
| `Action_None` | 84 | 145 | 62 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 9–13 | 5 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 99–269 | 171 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 102–269 | 155 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 109–269 | 131 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 115–124 | 10 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 115–172 | 18 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 121–210 | 38 | 4 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 129–269 | 111 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 136–269 | 80 | 4 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 147–269 | 123 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 162–207 | 37 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 167–269 | 103 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 176–214 | 27 | 4 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 193–269 | 62 | 3 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 214–269 | 43 | 4 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 221–269 | 37 | 3 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 224–229 | 6 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 259–269 | 11 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '17' has invalid range: start=94, end=85. Clamping end to start.
- ⚠️ Action 'Action_ZoneBlock' range [87-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-177] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-116] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [119-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [125-140] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-263] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [91-114] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-208] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-207] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-149] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-115] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-131] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-265] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [111-158] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-83] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-157] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-96] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-108] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-79] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' for track '15' starts at frame 84, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallSnap' range [84-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-137] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-157] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-185] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-220] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-131] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-159] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-204] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-240] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-171] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-203] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-220] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-186] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-207] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-186] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-214] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-220] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-232] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>