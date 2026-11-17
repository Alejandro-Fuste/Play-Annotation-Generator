# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_49`
- **Input XML**: `outputs/batch/Power/Power/Power_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [13-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-198] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-202] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-192] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-217] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-250] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-259] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-164] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-181] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-154] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-234] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-164] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-190] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-217] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-217] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-247] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-258] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-164] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-269] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-133] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-146] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-29] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-66] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-93] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-108] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-124] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-156] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-14] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-33] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-106] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-33] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-189] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-192] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-199] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [105-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-111] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-88] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-93] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-65] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-95] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-173] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-117] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-158] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-215] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-210] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-179] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-223] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-218] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-241] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-242] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-269] for track '31' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.