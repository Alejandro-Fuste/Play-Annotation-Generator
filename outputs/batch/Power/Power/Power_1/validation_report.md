# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_1`
- **Input XML**: `outputs/batch/Power/Power/Power_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [4-5] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-5] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-133] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [74-104] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [108-109] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-218] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-137] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-105] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-118] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-166] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [74-130] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-239] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-87] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-131] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-239] for track '16' has 6 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [74-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-154] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-165] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-109] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-93] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-235] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [74-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [91-95] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [98-99] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [101-104] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-92] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-128] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-17] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-27] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-128] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-206] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-239] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-175] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-194] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-233] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '34' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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