# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_138`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_138/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Overlapping action conflict at frame 87 for track '11': 'Action_PressEdge' vs 'Action_Keep'. Overriding with 'Action_Keep'.
> - Action 'Action_PreSnap' range [0-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-178] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-202] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-281] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-335] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-157] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-190] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-196] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-230] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-251] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-113] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-121] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-188] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-72] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-141] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-289] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-77] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-132] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-208] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-223] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-71] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-148] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-186] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-139] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-212] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-243] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [107-119] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-79] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-120] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-8] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-66] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-114] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-192] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-99] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-148] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-134] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-199] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-205] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-128] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-134] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-267] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-175] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-253] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-266] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-292] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-321] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-336] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-347] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-232] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-222] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-229] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-205] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-343] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-321] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-359] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-264] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-311] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-349] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-302] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-310] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-322] for track '33' has 2 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.