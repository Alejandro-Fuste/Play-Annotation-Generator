# Play-Annotation-Generator Annotation Review — OutRoutes_137

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_137`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `13` | `13` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `6` | `6` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `4` | `4` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `20` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `21` | `Group` | 0 | START | 0 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `13` | `13` | 34 | START | 34 | 153 |
| ✅ EXACT | `Action_PassBlock` | LT | `18` | `18` | 34 | START | 34 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `6` | `6` | 34 | START | 34 | 48 |
| ✅ EXACT | `Action_PassBlock` | RT | `8` | `8` | 34 | START | 34 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `9` | `9` | 34 | START | 34 | 44 |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | `4` | `4` | 40 | START | 40 | 125 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `2` | 40 | END | 40 | 40 |
| ✅ EXACT | `Action_ThrowPass` | QB | `2` | `2` | 94 | START | 94 | 104 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `4` | `4` | 126 | START | 126 | 135 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `4` | `4` | 136 | START | 136 | 269 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–256
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_None` | 41 | 93 | 53 | inferred_complete_timeline |
| `Action_ThrowPass` | 94 | 104 | 11 | inferred_complete_timeline |
| `Action_None` | 105 | 256 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_RunOutRoute` | 40 | 125 | 86 | inferred_complete_timeline |
| `Action_SecureCatch` | 126 | 135 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 269 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 269 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 87 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 153 | 120 | inferred_complete_timeline |
| `Action_PassBlock` | 163 | 165 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 48 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 69 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 74 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 94 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 44 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 269 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–49
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 49 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 90 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 119 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 269 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 103 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–172
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 172 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 269 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–261
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 261 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 248 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 269 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–31 | 32 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 26–28 | 3 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 40–194 | 153 | 3 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 42–45 | 4 | 1 | Undefined position; Undefined team |
| `26` | `26` | Position_Unknown | Team_Unknown | 90–190 | 95 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 107–227 | 110 | 6 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 108–269 | 160 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 130–139 | 5 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 131–218 | 55 | 8 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 149–171 | 18 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 190–256 | 35 | 7 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 213–269 | 56 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 63 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-256] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-119] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-269] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-48] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-54] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-69] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-94] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-49] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-44] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-153] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [163-165] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-248] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-103] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-87] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-261] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-28] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-42] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-140] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-194] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-45] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-190] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-125] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-131] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-135] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-145] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-131] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-139] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-134] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-145] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-152] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-159] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-163] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-193] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-210] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-218] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-152] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-171] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-193] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-200] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-211] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-222] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-240] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-251] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-256] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-214] for track '34' has 1 frames without a visible bounding box.
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