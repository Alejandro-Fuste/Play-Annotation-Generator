# Play-Annotation-Generator Annotation Review — RPO_152

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_152`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunPostRoute` | actor_track_id `20` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 96
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `1` | `1` | 26 | START | 26 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `10` | `10` | 26 | START | 26 | 85 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `13` | `13` | 26 | START | 26 | 78 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 26 | START | 26 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `9` | `9` | 26 | START | 26 | 91 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `6` | 27 | START | 27 | 40 |
| ✅ EXACT | `Action_PullBall` | QB | `6` | `6` | 41 | START | 41 | 61 |
| ✅ EXACT | `Action_ThrowPass` | QB | `6` | `6` | 82 | START | 82 | 91 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 26 | 2 | inferred_complete_timeline |
| `Action_ReadDefender` | 27 | 40 | 14 | inferred_complete_timeline |
| `Action_PullBall` | 41 | 61 | 21 | inferred_complete_timeline |
| `Action_None` | 62 | 81 | 20 | inferred_complete_timeline |
| `Action_ThrowPass` | 82 | 91 | 10 | inferred_complete_timeline |
| `Action_None` | 92 | 104 | 13 | inferred_complete_timeline |
| `Action_None` | 106 | 150 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 226 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 39 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 25 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 91 | 66 | inferred_complete_timeline |
| `Action_None` | 92 | 143 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 25 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 59 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 91 | 12 | inferred_complete_timeline |
| `Action_None` | 92 | 98 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 25 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 85 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 92 | 97 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 25 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 78 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 25 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 26 | 91 | 66 | inferred_complete_timeline |
| `Action_None` | 92 | 100 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 72 | 48 | inferred_complete_timeline |
| `Action_None` | 85 | 107 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 37 | 125 | 89 | inferred_complete_timeline |
| `Action_None` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_None` | 134 | 139 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 48 | 24 | inferred_complete_timeline |
| `Action_None` | 51 | 103 | 53 | inferred_complete_timeline |
| `Action_None` | 121 | 123 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 53 | 29 | inferred_complete_timeline |
| `Action_None` | 57 | 93 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 24 | 4 | inferred_complete_timeline |
| `Action_None` | 25 | 51 | 27 | inferred_complete_timeline |
| `Action_None` | 53 | 69 | 17 | inferred_complete_timeline |
| `Action_None` | 75 | 80 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 145 | 121 | inferred_complete_timeline |
| `Action_None` | 147 | 329 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 92 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 49–101 | 47 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 52–59 | 8 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 90–329 | 236 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 91–101 | 7 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 95–101 | 7 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 95–96 | 2 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 101–151 | 51 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 107–112 | 5 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 107–145 | 17 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 110–329 | 220 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 115–158 | 42 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 117–189 | 73 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 121–262 | 116 | 9 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 125–140 | 16 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 131–329 | 199 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 131–141 | 11 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 134–154 | 19 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 138–149 | 12 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 151–318 | 155 | 5 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 183–329 | 147 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 199–226 | 27 | 2 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 205–254 | 50 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 245–254 | 10 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 283–325 | 26 | 4 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 287–322 | 36 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 289–298 | 10 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 302–329 | 28 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 80 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [25-39] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-59] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-76] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-92] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-143] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-145] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-53] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-93] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-150] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-226] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-51] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-91] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-100] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-85] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-107] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-48] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [26-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-125] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-139] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-101] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-59] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-314] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-145] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-329] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-145] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-158] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-141] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-173] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-186] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-262] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-140] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-141] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-149] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-149] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-318] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-226] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-254] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-254] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-298] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-308] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-322] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-298] for track '41' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.

</details>