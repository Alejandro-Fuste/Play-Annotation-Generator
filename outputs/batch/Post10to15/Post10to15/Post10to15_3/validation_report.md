# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_3`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [19–35], lower_priority='Action_PassBlock' annotated_start=22, effective_Action_PassBlock_start=36.
> - Action 'Action_None' range [19-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-65] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-172] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [36-166] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-114] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-181] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [19-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-46] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-107] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [109-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-139] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-78] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-85] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-155] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-158] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-188] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-65] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-118] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [125-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-156] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-167] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [36-210] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [93-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-127] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-50] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-192] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-127] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [130-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [136-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-8] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-39] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-84] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-193] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-107] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-192] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-131] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-189] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-136] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-156] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-191] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-185] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.