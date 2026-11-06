# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_8`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-116] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-134] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-142] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-184] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-139] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-266] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-185] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [67-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-266] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-132] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-78] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-202] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-146] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-154] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-191] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-9] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-23] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-135] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-207] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-151] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-103] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-96] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-146] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-177] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-146] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-184] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-178] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-199] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-232] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-230] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-244] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-252] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.