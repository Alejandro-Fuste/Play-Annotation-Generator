# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_25`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [24-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-47] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-54] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [90-92] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-196] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-175] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-188] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [79-188] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [24-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [45-76] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-90] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [92-100] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-182] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-158] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-62] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-198] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-202] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-209] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-187] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-174] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [178-180] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-184] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-199] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '34' has 2 frames without a visible bounding box.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.