# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_298`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_298/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 598: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '1' (Unknown) duration 99 frames exceeds threshold 90 frames [start=108, end=206].
> - Validation warning: Action 'Action_DownBlock' for track '4' (LT) duration 99 frames exceeds threshold 90 frames [start=108, end=206].
> - Segment 'Action_BallCarry' for track '5' has invalid range: start=153, end=149. Clamping end to start.
> - Validation warning: Action 'Action_DownBlock' for track '7' (LG) duration 99 frames exceeds threshold 90 frames [start=108, end=206].
> - Validation warning: Action 'Action_PullBlock' for track '8' (RG) duration 99 frames exceeds threshold 90 frames [start=108, end=206].
> - Segment 'Action_SnapReceive' for track '14' has invalid range: start=105, end=100. Clamping end to start.
> - Segment 'Action_Handoff' for track '14' has invalid range: start=124, end=100. Clamping end to start.
> - Action 'Action_None' range [105-183] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [108-118] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [123-138] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [108-206] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [108-142] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [167-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-126] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-133] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [108-149] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [108-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-124] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [105-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-159] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-33] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-69] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-94] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-94] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-224] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-233] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-204] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-197] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-241] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-233] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-252] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-266] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-220] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-228] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-254] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-259] for track '30' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.