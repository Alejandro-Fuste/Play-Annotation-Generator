# Play-Annotation-Generator Annotation Review — OutRoutes_153

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_153`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 123
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
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunOutRoute` | WR4 | offense | `1` | `1` |
| ✅ EXACT | `Action_RunOutRoute` | DE1 | defense | `3` | `3` |
| ✅ EXACT | `Action_RunOutRoute` | SAF | defense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_SecureCatch` | DE1 | defense | `3` | `3` |
| ✅ EXACT | `Action_BallCarry` | DE1 | defense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `10` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `14` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 11 | START | 11 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `17` | 11 | START | 11 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 11 | START | 11 | 46 |
| ✅ EXACT | `Action_PassBlock` | RG | `19` | `19` | 11 | START | 11 | 57 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 11 | START | 11 | 57 |
| ✅ EXACT | `Action_RunOutRoute` | WR4 | `1` | `1` | 16 | START | 16 | 180 |
| ✅ EXACT | `Action_RunOutRoute` | DE1 | `3` | `3` | 16 | START | 16 | 73 |
| ✅ EXACT | `Action_RunOutRoute` | SAF | `4` | `4` | 16 | START | 16 | 65 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 16 | END | 16 | 16 |
| ✅ EXACT | `Action_ThrowPass` | QB | `7` | `7` | 52 | START | 52 | 57 |
| ✅ EXACT | `Action_SecureCatch` | DE1 | `3` | `3` | 74 | START | 74 | 93 |
| ✅ EXACT | `Action_BallCarry` | DE1 | `3` | `3` | 94 | START | 94 | 136 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 16 | 1 | inferred_complete_timeline |
| `Action_None` | 17 | 51 | 35 | inferred_complete_timeline |
| `Action_ThrowPass` | 52 | 57 | 6 | inferred_complete_timeline |
| `Action_None` | 58 | 131 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunOutRoute` | 16 | 180 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 42 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 60 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 93 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 107 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 109 | 110 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 57 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 43 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 57 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 46 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 173 | 107 | inferred_complete_timeline |
| `Action_PassBlock` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunOutRoute` | 16 | 73 | 58 | inferred_complete_timeline |
| `Action_SecureCatch` | 74 | 93 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 136 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 180 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 97 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 174 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 180 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 127 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 151 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 167 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 176 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 159 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunOutRoute` | 16 | 65 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–55 | 55 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 40–47 | 8 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 44–46 | 3 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 63–138 | 76 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 68–157 | 11 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 75–180 | 94 | 7 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 76–78 | 3 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 99–101 | 3 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 106–124 | 12 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 135–136 | 2 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 136–180 | 40 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 138–174 | 14 | 3 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 138–179 | 14 | 2 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 145–147 | 3 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 153–180 | 28 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 162–180 | 19 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 162–163 | 2 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 167–174 | 8 | 1 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 169–171 | 3 | 1 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 170–177 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 81 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [16-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [16-73] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-136] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [16-65] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-127] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-131] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-148] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-97] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [128-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-167] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-176] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-42] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-60] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-107] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [109-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-46] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-50] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-58] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-173] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [178-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-55] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-47] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-46] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-138] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-71] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-79] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-157] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-83] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-94] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-98] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-105] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-78] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-101] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-107] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-116] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-124] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-136] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-148] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-168] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-180] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-140] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-148] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-174] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-147] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-179] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-147] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-180] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-180] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-174] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-171] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-177] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.

</details>