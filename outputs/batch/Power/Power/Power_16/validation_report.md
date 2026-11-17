# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_16`
- **Input XML**: `outputs/batch/Power/Power/Power_16/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [72-127] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [72-86] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [72-80] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-123] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-113] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-151] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-149] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-205] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-166] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-192] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-160] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-168] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-149] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-164] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-177] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-186] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-192] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-197] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-172] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-185] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-210] for track '31' has 1 frames without a visible bounding box.
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