# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_115`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_115/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-229] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-176] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-184] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-205] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-217] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-145] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-239] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [137-170] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-239] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-31] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-239] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-176] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-239] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-40] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-43] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-220] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-183] for track '14' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-225] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-239] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-239] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-215] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-24] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-143] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-161] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-176] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-182] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-239] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-183] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-239] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-182] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-239] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-217] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-223] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-239] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-239] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-220] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-239] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-196] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-199] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-218] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-239] for track '29' has 1 frames without a visible bounding box.
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