# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_332`
- **Input XML**: `outputs/batch/Power/Power/Power_332/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '2' (RG) duration 102 frames exceeds threshold 90 frames [start=129, end=230].
> - Validation warning: Action 'Action_DownBlock' for track '6' (RT) duration 98 frames exceeds threshold 90 frames [start=129, end=226].
> - Validation warning: Action 'Action_DownBlock' for track '12' (C) duration 102 frames exceeds threshold 90 frames [start=129, end=230].
> - Action 'Action_PreSnap' range [4-199] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-274] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-293] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [129-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [158-160] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [194-228] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-264] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-292] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-185] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-222] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-290] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [129-131] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [142-148] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [156-160] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-152] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-158] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [129-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [144-154] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [157-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [173-226] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-202] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-217] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-226] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-271] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-291] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-26] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-157] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-205] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-194] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-232] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-239] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [129-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [166-181] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [190-230] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-160] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-216] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-270] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-192] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-228] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-280] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-240] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-192] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-216] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-278] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-257] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-273] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-264] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-280] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-298] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '29' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.