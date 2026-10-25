# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_33`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 103 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [24-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-119] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [121-199] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-104] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-156] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-115] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [37-52] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-193] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-52] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-89] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-113] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-139] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-100] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [104-107] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-113] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-203] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-193] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-172] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [37-115] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [24-176] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-196] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [37-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [69-80] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [98-115] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 187, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [187-199] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [37-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [85-113] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [122-123] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [135-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [141-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [37-83] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-138] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-188] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-119] for track '25' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [121-136] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [136-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-210] for track '28' has 1 frames without a visible bounding box.
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