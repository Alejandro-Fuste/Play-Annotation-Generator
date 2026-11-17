# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_70`
- **Input XML**: `outputs/batch/Power/Power/Power_70/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 141: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 142: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_DownBlock' range [87-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-197] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-116] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [87-101] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [108-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [122-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-195] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-84] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-84] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-87] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-84] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-155] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-195] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-33] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-106] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-59] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-167] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-151] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-30] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-135] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-154] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-184] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-192] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-86] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [87-95] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-110] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-56] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [87-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [111-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-76] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-147] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-152] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-145] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-172] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-194] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-172] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-193] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-207] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-181] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-187] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-161] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-200] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-163] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-185] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-201] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-191] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-209] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-210] for track '25' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.