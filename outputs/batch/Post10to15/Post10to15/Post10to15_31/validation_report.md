# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_31`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_31/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [35-195] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-209] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-127] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-174] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [36-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-86] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-137] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-71] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [74-181] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-142] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [35-48] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-53] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-201] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-109] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-172] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [35-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-161] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-140] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-89] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-112] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [118-182] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-157] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-122] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-167] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-109] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-122] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-186] for track '29' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.