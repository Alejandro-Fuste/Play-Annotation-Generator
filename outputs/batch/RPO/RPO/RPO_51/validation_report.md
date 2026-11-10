# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_51`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [62-206] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-241] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [74-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-102] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-113] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-239] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-110] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-269] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-99] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-107] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-61] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-69] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-269] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-61] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-99] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-100] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-126] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-132] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-178] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-172] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-218] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.